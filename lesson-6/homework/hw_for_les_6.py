# ### Zero Check Decorator
# Write a decorator function called `check` that verifies that the denominator is not equal to 0 and apply it to the following function:

# ```python
# @check
# def div(a, b):
#    return a / b
# ```

# ```
# input: div(6, 2)
# output: 3
# ```

# ```
# input: div(6, 0)
# output: "Denominator can't be zero"
# ```

def check(func):
    '''Decorator function that checks if denominator is zero.'''
    def wrapper(a, b):
        try:
            return func(a, b)
        except ZeroDivisionError:
            return "Denominator can't be zero"
    return wrapper

@check
def div(a, b):
    '''Function for division.'''
    return a / b

# Testing the function
print(div(6, 0))   # Output: "Denominator can't be zero"
print(div(6, 2))   # Output: 3.0
print(div(6, 3))   # Output: 2.0




# ### **Employee Records Manager**
# **Objective**: Create a program to manage employee records using file handling.  

# **Tasks**:  
# 1. **File Creation and Data Entry**  
#    - Create a file named **"employees.txt"**.  
#    - Allow the user to add new employee records. Each record should have the following fields:  
#      ```
#      Employee ID, Name, Position, Salary
#      ```
#      Example of a record:  
#      ```
#      1001, John Doe, Software Engineer, 75000
#      ```

with open("employees.txt","wt") as file:
    while True:
        emp_id=int(input("Please enter the employee ID: "))
        name=input("Enter the name of employee: ")
        position=input("Enter the position of employee: ")
        salary=float(input("Enter the salary: "))
        record=f"{emp_id}, {name}, {position}, {salary}\n"
        file.write(record) 

        answer=input("Do you want to add new employee records? yes/y or no/n: ")
        if answer in ['no','n']:
            break 

reading=open('employees.txt', 'r')
print(reading.read()) 



# 2. **Menu Options**  
#    Your program should present the following options:  
#    ```
#    1. Add new employee record
#    2. View all employee records
#    3. Search for an employee by Employee ID
#    4. Update an employee's information
#    5. Delete an employee record
#    6. Exit
#    ```


# Decorator to check if Employee ID exists before updating or deleting
def check_employee_exists(func):
    def wrapper(emp_id, *args, **kwargs):
        with open("employees.txt", "r") as file:
            records = file.readlines()

        if not any(line.startswith(str(emp_id) + ",") for line in records):
            return "Employee ID not found." 
        return func(emp_id, *args, **kwargs)
    return wrapper



# Function to add an employee
def adding_emp():
    """Adding new employee records with unique Employee ID"""
    emp_id = input("Enter Employee ID: ")
    
    with open("employees.txt", "r") as file:
        records = file.readlines()
        for record in records:
            if record.startswith(emp_id + ","):    ### ID should be unique, so it is checking if this ID is already exist
                print("Error: Employee ID already exists! Try again.")
                return 

    # If ID is unique, proceed with adding
    name = input("Enter Employee Name: ")
    position = input("Enter Employee Position: ")
    salary = input("Enter Employee Salary: ")
    with open("employees.txt", "a") as file:
        record = f"{emp_id}, {name}, {position}, {salary}\n"
        file.write(record)
    
    print("Employee record added successfully!")



# Function to view all employee records
def view_records():
    """Display all employee records"""
    with open("employees.txt", "r") as file:
        records = file.readlines()

    if records:
        print("\nEmployee Records:")
        for record in records:
            print(record.strip())
    else:
        print("No records found.") 

# Function to search for an employee by ID
def search_emp(emp_id):
    """Search for an employee by Employee ID"""
    with open("employees.txt", "r") as file:
        records = file.readlines()

    for record in records:
        if record.startswith(emp_id + ","):
            print("Employee Found:", record.strip())
            break 
    else:
        print("Employee ID not found.")


# Function to update an employee's information
@check_employee_exists   # decorator function helps to checking ID is found or not
def update_emp(emp_id):
    """Update an employee's details"""
    with open("employees.txt", "r") as file:
        records = file.readlines()

    with open("employees.txt", "w") as file:
        for record in records:
            if record.startswith(str(emp_id) + ","):
                name = input("Enter new name: ")
                position = input("Enter new position: ")
                salary = input("Enter new salary: ")
                updated_record = f"{emp_id}, {name}, {position}, {salary}\n"
                file.write(updated_record)
                print("Employee details updated successfully!")
            else:      ### write deletes all other lines so there is line of else code. It adds other lines again to the file
                file.write(record)      

# Function to delete an employee record
@check_employee_exists     # decorator function helps to checking ID is found or not
def delete_emp(emp_id):
    """Delete an employee record"""
    with open("employees.txt", "r") as file:
        records = file.readlines()

    with open("employees.txt", "w") as file:
        for record in records:
            if not record.startswith(str(emp_id) + ","):
                file.write(record) 
    print("Employee record deleted successfully!")


# Main Menu Loop
while True:
    print("""Choose one of the options below to continue: 
    1. Add new employee record"
    2. View all employee records"
    3. Search for an employee by Employee ID"
    4. Update an employee's information"
    5. Delete an employee record"
    6. Exit """)

    choice = input("Choose an option (1-6): ")
        
    if choice == "1":
        adding_emp()
    elif choice == "2":
        view_records()
    elif choice == "3":
        emp_id = input("Enter Employee ID to search: ")
        search_emp(emp_id)
    elif choice == "4":
        emp_id = input("Enter Employee ID to update: ")
        update_emp(emp_id)  
    elif choice == "5":
        emp_id = input("Enter Employee ID to delete: ")
        delete_emp(emp_id)
    elif choice == "6":
        print("Exiting program. Goodbye!")
        break
    else:
        print("Invalid choice. Please enter a number between 1 and 6.")


# 3. **Functional Requirements**  
#    - **Option 1**: Append a new employee record to **"employees.txt"**.  
#    - **Option 2**: Display all employee records from **"employees.txt"**.  
#    - **Option 3**: Allow the user to search for an employee by **Employee ID** and display their details.  
#    - **Option 4**: Update an employee’s information (name, position, or salary) based on the Employee ID.  
#    - **Option 5**: Delete an employee's record from the file using the Employee ID.  
#    - **Option 6**: Exit the program. 

# ### **Word Frequency Counter**
# **Objective**: Analyze a text file and count how often each word appears.  

# **Tasks**:  
# 1. **File Input**  
#    - Use the file **"sample.txt"**. The file can contain any text (like a paragraph or an article).  
#    - If **"sample.txt"** does not exist, prompt the user to create it by typing in a paragraph.  

# 2. **Count Word Frequency**  
#    - Read the file content and split it into individual words.  
#    - Count the frequency of each word (ignore capitalization, e.g., "The" and "the" should be counted as the same word).  
#    - Ignore punctuation (like commas, periods, etc.).  

# 3. **Output**  
#    - Display the total number of words in the file.  
#    - Display the top 5 most common words with their counts.  
#    - Save the output to a new file called **"word_count_report.txt"**.  

# 4. **Example Output**  
#    **Content of sample.txt**:  
#    ```
#    This is a simple file.
#    This file, is for testing purposes. It is a test file.
#    ```

#    **Console Output**:  
#    ```
#    Total words: 14
#    Top 5 most common words:
#    is - 3 times
#    this - 2 times
#    file - 3 times
#    a - 2 times
#    test - 1 time
#    ```

#    **Content of word_count_report.txt**:  
#    ```
#    Word Count Report
#    Total Words: 14
#    Top 5 Words:
#    is - 3
#    file - 3
#    this - 2
#    a - 2
#    test - 1
#    ```


import os
import re

#  Check if file exists, if not, create it
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as file:
        message = input("Type something for the file: ")
        file.write(message)

# Read the file content
with open("sample.txt", "r") as file:
    content = file.read()

# Remove punctuation & convert to lowercase
content = re.sub(r"[^\w\s]", "", content).lower()  # Remove punctuation
words = content.split()  # Split into words


# Count word frequency using a dictionary
word_count = {}
for word in words: 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1  # Increase count


# Sort dictionary by word frequency (highest first)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

# Write results to word_count_report.txt
with open("word_count_report.txt", "w") as file:
    file.write(f"Total words: {len(words)}\n\n")
    file.write("Top 5 most common words:\n")
    for word, count in sorted_words[0:5]:  # Get top 5 words
        file.write(f"{word}: {count}\n")

# Display results
with open("word_count_report.txt", "r") as file:
    result=file.readlines()
    for i in result:
        print(i, end='')



# **Bonus Task**:  
# - Allow the user to specify how many "top common words" to display (e.g., top 3, top 10, etc.).  
# - Make sure the program ignores case, punctuation, and handles large files efficiently.  



import os
import re

#  Check if file exists, if not, create it
if not os.path.exists("sample.txt"):
    with open("sample.txt", "w") as file:
        message = input("Type something for the file: ")
        file.write(message)

# Read the file content
with open("sample.txt", "r") as file:
    content = file.read()

# Remove punctuation & convert to lowercase
content = re.sub(r"[^\w\s]", "", content).lower()  # Remove punctuation
words = content.split()  # Split into words


# Count word frequency using a dictionary
word_count = {}
for word in words: 
    if word in word_count:
        word_count[word] += 1
    else:
        word_count[word] = 1  # Increase count


# Sort dictionary by word frequency (highest first)
sorted_words = sorted(word_count.items(), key=lambda x: x[1], reverse=True)

number_of_words=int(input("How many top common words do you want to see? "))

# Write results to word_count_report.txt
with open("word_count_report.txt", "w") as file:
    file.write(f"Total words: {len(words)}\n\n")
    file.write("Top 5 most common words:\n")
    for word, count in sorted_words[0:number_of_words]:  # Get top given number of words
        file.write(f"{word}: {count}\n")

# Display results
with open("word_count_report.txt", "r") as file:
    result=file.readlines()
    for i in result:
        print(i, end='')