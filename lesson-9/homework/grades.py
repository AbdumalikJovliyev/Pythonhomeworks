# #### Task 2: Student Grades Management
# 1. Create a CSV file named `grades.csv` with the following structure:
#    ```csv
#    Name,Subject,Grade
#    Alice,Math,85
#    Bob,Science,78
#    Carol,Math,92
#    Dave,History,74
#    ```

# 2. Write a Python program to:
#    - Read data from `grades.csv` and store it in an appropriate data structure (e.g., a list of dictionaries).
#    - Calculate the average grade for each subject.
#    - Write a new CSV file named `average_grades.csv` with the following structure:
#      ```csv
#      Subject,Average Grade
#      Math,88.5
#      Science,78
#      History,74
#      ```
# 3. Use the `csv` module for reading and writing the CSV files.

import csv
import os
from collections import defaultdict

class GradeManager:
    def __init__(self, filename):
        self.filename = filename
        self.grades = []
        self.ensure_file_exists()

    def ensure_file_exists(self):
        """Creates the file with default data if it doesn't exist."""
        if not os.path.exists(self.filename):
            with open(self.filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Name", "Subject", "Grade"])
                writer.writerows([
                    ["Alice", "Math", 85],
                    ["Bob", "Science", 78],
                    ["Carol", "Math", 92],
                    ["Dave", "History", 74]])

    def read_grades(self):
        """Reads grades from the CSV file and stores them in a list of dictionaries."""
        try:
            with open(self.filename, newline='', mode='r') as file:
                reader = csv.DictReader(file)
                self.grades = [{"Name": row["Name"], "Subject": row["Subject"], "Grade": int(row["Grade"])} for row in reader]
        except Exception as e:
            print(f"Error reading file: {e}")
    
    def calculate_average(self, subject=None):
        """Calculates the average grade for each subject or a specific subject."""
        subject_totals = defaultdict(lambda: [0, 0])  # {subject: [total_grade, count]}
        for entry in self.grades:
            subject_totals[entry["Subject"]][0] += entry["Grade"]
            subject_totals[entry["Subject"]][1] += 1
        
        averages = {subj: round(total / count, 2) for subj, (total, count) in subject_totals.items()}
        return averages if subject is None else {subject: averages.get(subject, "Subject not found")}
    
    def write_average_grades(self, output_filename):
        """Writes the average grades to a new CSV file."""
        try:
            averages = self.calculate_average()
            with open(output_filename, mode='w', newline='') as file:
                writer = csv.writer(file)
                writer.writerow(["Subject", "Average Grade"])
                for subject, avg in averages.items():
                    writer.writerow([subject, avg])
            print(f"Average grades have been written to {output_filename}")
        except Exception as e:
            print(f"Error writing file: {e}")
    
    def add_grade(self, name, subject, grade):
        """Adds a new grade to the CSV file."""
        try:
            with open(self.filename, mode='a', newline='') as file:
                writer = csv.writer(file)
                writer.writerow([name, subject, grade])
            self.grades.append({"Name": name, "Subject": subject, "Grade": grade})
            print(f"Added grade: {name} - {subject}: {grade}")
        except Exception as e:
            print(f"Error writing file: {e}")
    
    def get_grades_by_name(self, name):
        """Gets all grades for a specific student."""
        results = [entry for entry in self.grades if entry["Name"].lower() == name.lower()]
        return results if results else "No records found."
    
    def display_all_grades(self):
        """Displays all records."""
        for entry in self.grades:
            print(entry)

def main_menu():
    grade_manager = GradeManager("grades.csv")
    grade_manager.read_grades()
    
    while True:
        print("\nWelcome to Student Grades Management System")
        print("1. View all grades")
        print("2. Add a new grade")
        print("3. Get grades for a specific student")
        print("4. Get the average grade for a subject or all subjects")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            grade_manager.display_all_grades()
        elif choice == "2":
            name = input("Enter student name: ")
            subject = input("Enter subject: ")
            try:
                grade = int(input("Enter grade: "))
                grade_manager.add_grade(name, subject, grade)
            except ValueError:
                print("Invalid grade input. Please enter a number.")
        elif choice == "3":
            name = input("Enter student name: ")
            print(grade_manager.get_grades_by_name(name))
        elif choice == "4":
            subject = input("Enter subject (or press Enter for all subjects): ")
            averages = grade_manager.calculate_average(subject if subject else None)
            print(averages)
        elif choice == "5":
            print("Exiting program...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main_menu()