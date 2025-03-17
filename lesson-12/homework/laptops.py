# ### Task 3
# You are tasked with scraping laptop data from the "Laptops" section of the [Demoblaze website](https://www.demoblaze.com/) and storing the extracted information in JSON format.
# **Steps:**
# 1. **Navigate to the Website:**
#    - Visit the [Demoblaze homepage](https://www.demoblaze.com/).
#    - Click on the **Laptops** section to view the list of available laptops.

# 2. **Navigate to the Next Page:**
#    - After reaching the Laptops section, locate and click the **Next** button to navigate to the next page of laptop listings.

# 3. **Data to Scrape:**
#    For each laptop on the page, scrape the following details:
#    - **Laptop Name**
#    - **Price**
#    - **Description**

# 4. **Data Storage:**
#    - Save the extracted information in a structured **JSON format** with fields like:
#      ```json
#      [
#        {
#          "name": "Laptop Name",
#          "price": "Laptop Price",
#          "description": "Laptop Description"
#        },
#      ]

import json
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException, TimeoutException, ElementClickInterceptedException


class LaptopScraper:
    def __init__(self, url):
        """Initialize the web driver and navigate to the site."""
        chrome_options = Options()
        chrome_options.add_argument("--disable-popup-blocking")
        chrome_options.add_experimental_option("detach", True)
        
        self.driver = webdriver.Chrome(options=chrome_options)
        self.driver.get(url)
        time.sleep(3)  # Allow page to load

    def navigate_to_laptops(self):
        """Click on the Laptops category."""
        try:
            laptops_category = self.driver.find_element(By.CSS_SELECTOR, "a[onclick=\"byCat('notebook')\"]")  # finding the element by css_selector
            laptops_category.click()
            time.sleep(3)  # Wait for content to load
        except NoSuchElementException:
            print("Laptops category not found. Exiting.")
            self.driver.quit()
            return False
        return True

    def scrape_page(self):
        """Scrape laptop data from the current page."""
        laptop_list = []
        try:
            laptops = self.driver.find_elements(By.CSS_SELECTOR, '[class="col-lg-4 col-md-6 mb-4"]')   # finding the element by css_selector
            for laptop in laptops:
                try:
                    title = laptop.find_element(By.CSS_SELECTOR, "h4.card-title a").text    # finding the element by css_selector
                    price = laptop.find_element(By.CSS_SELECTOR, "h5").text
                    description = laptop.find_element(By.CSS_SELECTOR, "p").text
                    laptop_list.append({
                        "name": title,
                        "price": price,
                        "description": description
                    })
                except NoSuchElementException:
                    print("A laptop element is missing details.")
        except NoSuchElementException:
            print("No laptops found on this page.")

        return laptop_list

    def scrape_all_pages(self):
        """Scrape all pages by clicking 'Next' when available."""
        all_laptops = []

        while True:
            all_laptops.extend(self.scrape_page())  # Scrape current page

            # Try to click next button if available
            try:
                next_page = self.driver.find_element(By.ID, "next2")
                if next_page.is_displayed():
                    next_page.click()
                    time.sleep(3)  #  Waiting for the next page to load
                else:
                    break  # Exit loop if "Next" button is not visible
            except (NoSuchElementException, ElementClickInterceptedException):
                print("No more pages to scrape.")
                break     # Exiting loop when there is no "Next" button

        return all_laptops

    def save_to_json(self, data, filename="laptops.json"):
        """Save the scraped data to a JSON file."""
        with open(filename, "w", encoding="utf-8") as json_file:
            json.dump(data, json_file, indent=4, ensure_ascii=False)
        print(f"Data saved successfully in {filename}")

    def close_browser(self):
        """Close the Selenium browser."""
        self.driver.quit()

# --- Run the Scraper ---
if __name__ == "__main__":
    scraper = LaptopScraper("https://www.demoblaze.com/")
    
    if scraper.navigate_to_laptops():
        laptops_data = scraper.scrape_all_pages()
        scraper.save_to_json(laptops_data)

    scraper.close_browser()