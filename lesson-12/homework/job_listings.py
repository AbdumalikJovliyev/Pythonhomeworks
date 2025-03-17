# ### Task 2

# Scrape job listings from the website https://realpython.github.io/fake-jobs and store the data into an SQLite database.

# 1. **Scraping Requirements**:
#    - Extract the following details for each job listing:
#      - **Job Title**
#      - **Company Name**
#      - **Location**
#      - **Job Description**
#      - **Application Link**

# 2. **Data Storage**:
#    - Store the scraped data into an SQLite database in a table named `jobs`.

# 3. **Incremental Load**:
#    - Ensure that your script performs **incremental loading**:
#      - Scrape the webpage and add only **new job listings** to the database.
#      - Avoid duplicating entries. Use `Job Title`, `Company Name`, and `Location` as unique identifiers for comparison.

# 4. **Update Tracking**:
#    - Add functionality to detect if an existing job listing has been updated (e.g., description or application link changes) and update the database record accordingly.

# 5. **Filtering and Exporting**:
#    - Allow filtering job listings by **location** or **company name**.
#    - Write a function to export filtered results into a CSV file.

import requests
import sqlite3
import csv
from bs4 import BeautifulSoup

# URL to scrape
URL = "https://realpython.github.io/fake-jobs/"

# Function to fetch job description from apply link
def description(url):
    """Get the job description from the apply page."""
    try:
        apply_page = requests.get(url)
        soup = BeautifulSoup(apply_page.content, "html.parser")
        results = soup.find(id="ResultsContainer")
        classes = results.find_all("div", class_="box")
        for descr in classes:
            if descr.find('div', class_='content'):
                return descr.find('p').text  
    except:
        return "Description not available"

# Connect to SQLite database
conn = sqlite3.connect("jobs.db")
cursor = conn.cursor()

# Create table if not exists
cursor.execute("""
CREATE TABLE IF NOT EXISTS jobs (
    Job_Title TEXT,
    Company_Name TEXT,
    Location TEXT,
    Description TEXT,
    Link TEXT
);
""")
conn.commit()

# Function to scrape and store job listings
def scrape_jobs():
    """Scrape job listings and store them in the database (incremental loading)."""
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, "html.parser")
    results = soup.find(id="ResultsContainer")
    job_cards = results.find_all("div", class_="card-content")

    for job_card in job_cards:
        try:
            title_element = job_card.find("h2", class_="title")
            company_element = job_card.find("h3", class_="company")
            location_element = job_card.find("p", class_="location")

            if not title_element or not company_element or not location_element:
                continue

            links = job_card.find_all("a")
            if len(links) < 2:
                continue

            link_url = links[1]["href"]
            job_description = description(link_url)
            job_title = title_element.text.strip()
            company_name = company_element.text.strip()
            location = location_element.text.strip()

            # Check if job already exists
            cursor.execute("""
            SELECT Description, Link FROM jobs 
            WHERE Job_Title = ? AND Company_Name = ? AND Location = ?;
            """, (job_title, company_name, location))

            result = cursor.fetchone()

            if result is None:  # If job does not exist, insert it
                cursor.execute("""
                INSERT INTO jobs (Job_Title, Company_Name, Location, Description, Link) 
                VALUES (?, ?, ?, ?, ?);
                """, (job_title, company_name, location, job_description, link_url))
                conn.commit()

            else:
                # Update if description or link has changed
                existing_description, existing_link = result
                if existing_description != job_description or existing_link != link_url:
                    cursor.execute("""
                    UPDATE jobs 
                    SET Description = ?, Link = ? 
                    WHERE Job_Title = ? AND Company_Name = ? AND Location = ?;
                    """, (job_description, link_url, job_title, company_name, location))
                    conn.commit()
                    print(f"Updated job: {job_title} at {company_name}")

        except Exception as e:
            print(f"Error processing job: {e}")

# Function to filter jobs and export to CSV
def filter_and_export_jobs(location=None, company_name=None):
    """Filter jobs by location or company name and save to CSV (without modifying DB)."""
    query = "SELECT * FROM jobs WHERE 1=1"
    params = []

    if location:
        query += " AND Location LIKE ?"
        params.append(f"%{location}%")
    if company_name:
        query += " AND Company_Name LIKE ?"
        params.append(f"%{company_name}%")

    cursor.execute(query, params)
    filtered_jobs = cursor.fetchall()

    if not filtered_jobs:
        print("No jobs found with the given filter.")
        return

    # Save to CSV
    with open("filtered_jobs.csv", "w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Job Title", "Company Name", "Location", "Description", "Link"])
        writer.writerows(filtered_jobs)

    print("Filtered jobs saved to 'filtered_jobs.csv'.")

# Function to view jobs in the database
def view_jobs():
    """Display all job listings stored in the database."""
    cursor.execute("SELECT Job_Title, Company_Name, Location, Link FROM jobs")
    jobs = cursor.fetchall()

    if not jobs:
        print("No job listings found in the database.")
        return

    print("\n--- Job Listings ---")
    for job in jobs:
        print(f"{job[0]} at {job[1]} ({job[2]}) link for applying: {job[3]}")
    print("\n")

# Main menu for user interaction
def main():
    while True:
        print("\n--- Job Scraper Menu ---")
        print("1. Scrape and store job listings")
        print("2. Filter and export jobs to CSV")
        print("3. View stored job listings")
        print("4. Exit")
        
        choice = input("Enter your choice: ")

        if choice == "1":
            scrape_jobs()
        elif choice == "2":
            loc = input("Enter location to filter (leave blank for all): ").strip()
            comp = input("Enter company name to filter (leave blank for all): ").strip()
            filter_and_export_jobs(loc if loc else None, comp if comp else None)
        elif choice == "3":
            view_jobs()
        elif choice == "4":
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

# Run the program
if __name__ == "__main__":
    main()