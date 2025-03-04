# ## Employee Records Manager (OOP Version)
# **Objective**: Create a program to manage employee records using classes and file handling.

# ### **Tasks and Requirements**

# 1. **Class Design**  
#    - Create a class `Employee` to represent individual employees with the following attributes:
#      - `employee_id`
#      - `name`
#      - `position`
#      - `salary`
#    - Create a class `EmployeeManager` to handle operations such as adding, viewing, searching, updating, and deleting employee records. This class will manage the file **"employees.txt"**.


# 2. **File Handling**  
#    - All employee records should be stored in **"employees.txt"**.  
#    - Each operation (add, view, update, delete) should interact with the file to ensure data persistence.

# 3. **Menu Options**  
#    Implement a menu within the `EmployeeManager` class with the following options:
#    ```
#    1. Add new employee record
#    2. View all employee records
#    3. Search for an employee by Employee ID
#    4. Update an employee's information
#    5. Delete an employee record
#    6. Exit
#    ```

# 4. **Functional Requirements**  
#    - **Option 1**: Add a new employee by creating an `Employee` object and appending it to **"employees.txt"**.  
#    - **Option 2**: Read all records from **"employees.txt"** and display them.  
#    - **Option 3**: Search for an employee by **Employee ID** and display their details.  
#    - **Option 4**: Update an employee's information (name, position, or salary) based on the Employee ID.  
#    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
#    - **Option 6**: Exit the program.


# ### **Example Usage**  
# ```plaintext
# Welcome to the Employee Records Manager!
# 1. Add new employee record
# 2. View all employee records
# 3. Search for an employee by Employee ID
# 4. Update an employee's information
# 5. Delete an employee record
# 6. Exit

# Enter your choice: 1
# Enter Employee ID: 1001
# Enter Name: John Doe
# Enter Position: Software Engineer
# Enter Salary: 75000
# Employee added successfully!

# Enter your choice: 2
# Employee Records:
# 1001, John Doe, Software Engineer, 75000

# Enter your choice: 3
# Enter Employee ID to search: 1001
# Employee Found:
# 1001, John Doe, Software Engineer, 75000

# Enter your choice: 6
# Goodbye!
# ```

# ### **Additional Instructions**
# 1. Use the `Employee` class to encapsulate individual employee data and functionality (e.g., a `__str__` method for displaying employee details).  
# 2. Use the `EmployeeManager` class for managing operations such as file handling, record searching, and updates.  
# 3. Ensure your code is modular, with methods for each operation (e.g., `add_employee`, `view_all_employees`).  


# ### **Bonus Challenge**
# 1. Add validation to ensure unique Employee IDs.   
# 2. Implement error handling for invalid inputs and file operations.  
# 3. Allow users to sort employee records (e.g., by salary or name) before displaying them.  



import os

class Employee:
    def __init__(self, emp_id, name, pos, salary):
        self.emp_id = emp_id
        self.name = name
        self.pos = pos
        self.salary = salary

    def __str__(self):
        return f"{self.emp_id}, {self.name}, {self.pos}, {self.salary}"


class EmployeeManager:
    def __init__(self):
        # Open file in append+ mode and keep it open for reuse
        if os.path.exists("employees.txt"):
            self.file = open("employees.txt", "a+")
        else:
            self.file = open("employees.txt", "w+")

    # Method to get all records from the file
    def get_records(self):
        self.file.seek(0)
        records = self.file.readlines()
        return [tuple(map(str.strip, record.strip().split(","))) for record in records if record.strip()]

    def __str__(self):
        return str(self.get_records())     #  just dunder method to print all employees if needed. 

    # Method to add new employee
    def add_employee(self):
        emp_id = input("Enter Employee ID: ")
        # Check if employee ID already exists using get_records()
        records = self.get_records()
        if any(record[0] == emp_id for record in records):
            print("Error: Employee ID already exists! Try again.")
            return

        name = input("Enter Employee Name: ")
        position = input("Enter Employee Position: ")
        
        while True:            #  using while loop for getting desired type of data for salary variable: it should be float or integer not strings, list, etc
            salary = input("Enter Employee Salary: ").strip()
            if salary.isdigit() and int(salary) > 0:
                salary = int(salary)
                break
            else:
                print("Invalid salary! Please enter a positive integer.")
        
        self.file.write(f"{emp_id}, {name}, {position}, {salary}\n")   #  adding each given variable to the file  
        self.file.flush()
        print("Employee record added successfully!")

    def sorting_viewing_emps(self):
        records = self.get_records()
        
        if not records:
            print("No employee records found.")
            return

        choice = input("What should I sort by? (ID, Name, Salary): ").lower()

        try:
            if choice == "id":
                sorted_records = sorted(records, key=lambda x: int(x[0]))    #  sorting according IDs
            elif choice == "name":
                sorted_records = sorted(records, key=lambda x: x[1].lower())  #  sorting according to name
            elif choice == "salary":
                sorted_records = sorted(records, key=lambda x: float(x[3]), reverse=True)   #  sorting according to salary of the workers
            else:
                print("Invalid choice. Please enter ID, Name, or Salary.")
                return

            print("\nSorted Employee Records:")
            for record in sorted_records:
                print(", ".join(record))
        except (IndexError, ValueError):
            print("Error in sorting records due to invalid data.")

    def search_emp(self):     #  method for searching an employee
        records = self.get_records()
        if not records:
            print("No employee records found.")
            return

        try:
            emp_id = input("Enter Employee ID to search: ")    
            for record in records:      #  using loop for each line of the text file until the first element, meaning the ID is equal to given id. 
                if record[0] == emp_id: 
                    print("Employee Found:", ", ".join(record))
                    return
            print("Employee ID not found.")   
        except ValueError:
            print("Invalid input. Please enter a valid Employee ID.")  

    def check_employee_exists(func):      #  decorator function for checking the ID exists in the list of the employees
        def wrapper(self, emp_id, *args, **kwargs):
            records = self.get_records()
            if not any(record[0] == emp_id for record in records):
                print("Employee ID not found.")
                return
            return func(self, emp_id, *args, **kwargs)
        return wrapper

    @check_employee_exists
    def update_emp(self, emp_id):  #  method for updating information of employee 
        records = self.get_records()
        with open("employees.txt", "w") as file:
            for record in records:
                if record[0] == emp_id:
                    name = input("Enter new name: ")
                    position = input("Enter new position: ")
                    while True:
                        salary = input("Enter Employee Salary: ").strip()     #  using while loop for getting desired type of data for salary variable: it should be float or integer not strings, list, etc
                        if salary.isdigit() and int(salary) > 0:
                            salary = int(salary)
                            break
                        else:
                            print("Invalid salary! Please enter a positive integer.")

                    file.write(f"{emp_id}, {name}, {position}, {salary}\n")
                    print("Employee details updated successfully!")
                else:
                    file.write(", ".join(record) + "\n")

    @check_employee_exists        #  checking if ID exists using previously created decorator function 
    def delete_emp(self, emp_id):  #  method for deleting employee while given an ID of the employee
        records = self.get_records()
        with open("employees.txt", "w") as file:
            for record in records:
                if record[0] != emp_id:
                    file.write(", ".join(record) + "\n")
        print("Employee record deleted successfully!")

    def close(self):  #  for closing file once in the end of the program. 
        self.file.close()

    def main_menu(self):   #  main menu of the Employee Manager Records 
        while True:
            print("""\nWelcome to the Employee Records Manager!
            Choose one of the options below to continue: 
            1. Add new employee record
            2. View all employee records
            3. Search for an employee by Employee ID
            4. Update an employee's information
            5. Delete an employee record
            6. Exit """)

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                self.add_employee()
            elif choice == "2":
                self.sorting_viewing_emps()
            elif choice == "3":
                self.search_emp()
            elif choice == "4":
                emp_id = input("Enter Employee ID to update: ")
                self.update_emp(emp_id)
            elif choice == "5":
                emp_id = input("Enter Employee ID to delete: ")
                self.delete_emp(emp_id)
            elif choice == "6":
                print("Exiting program.")
                self.close()
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")   #  printing message for exceptions

# Run the program
a = EmployeeManager()
a.main_menu()
