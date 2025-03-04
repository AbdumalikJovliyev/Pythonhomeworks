# ## To-Do Application

# **Objective**: Create a flexible To-Do application to manage tasks with support for different file storage formats (e.g., CSV, JSON). The application should be designed such that adding support for a new file format requires minimal changes to the code.


# ### **Task Description**

# #### 1. Functional Requirements:
# Your To-Do application should provide the following features:
# 1. **Add a task**: Allow users to add tasks with the following details:
#    - `Task ID`
#    - `Title`
#    - `Description`
#    - `Due Date` (optional)
#    - `Status` (e.g., Pending, In Progress, Completed)
# 2. **View tasks**: Display all tasks with their details.
# 3. **Update a task**: Allow users to modify a task's details using its Task ID.
# 4. **Delete a task**: Remove a task by its Task ID.
# 5. **Filter tasks**: Filter tasks by status (e.g., Pending or Completed).
# 6. **Save and load tasks**: Save tasks to a file and load them from the file on startup.



# #### 2. Design Requirements:
# 1. **Separation of Concerns**:
# 2. **Support for Multiple Formats**:
# 3. **Minimal Code Changes**:

# #### 3. Example Usage:
# ```plaintext
# Welcome to the To-Do Application!
# 1. Add a new task
# 2. View all tasks
# 3. Update a task
# 4. Delete a task
# 5. Filter tasks by status
# 6. Save tasks
# 7. Load tasks
# 8. Exit

# Enter your choice: 1
# Enter Task ID: 101
# Enter Title: Finish Homework
# Enter Description: Complete math and science homework.
# Enter Due Date (YYYY-MM-DD): 2024-12-31
# Enter Status (Pending/In Progress/Completed): Pending
# Task added successfully!

# Enter your choice: 2
# Tasks:
# 101, Finish Homework, Complete math and science homework., 2024-12-31, Pending
# ```

# ### **Deliverables**
# 1. Python scripts with classes and methods implemented as described.
# 2. Clear comments and documentation. 
# 3. A brief explanation of how you ensured minimal code changes when adding support for new file formats.


    
# Abstract class for file handling
class FileHandler:
    def save_tasks(self, tasks):
        pass

    def load_tasks(self):
        pass
    
    # save tasks
    # load tasks
    # for different file formats




import csv
import json
# CSV implementation
class CSVHandler(FileHandler):
    def save_tasks(self, tasks):
        with open('tasks.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            # Writing headers
            writer.writerow(['Task ID', 'Title', 'Description', 'Due Date', 'Status'])
            # Writing task data
            for task in tasks:
                writer.writerow([task.task_id, task.title, task.description, task.due_date or 'N/A', task.status])
        print("Tasks saved to tasks.csv successfully!\n")

    def load_tasks(self):
        tasks = []
        try:
            with open('tasks.csv', mode='r') as file:
                reader = csv.DictReader(file)
                for row in reader:
                    # Handling 'N/A' for due date
                    due_date = row['Due Date'] if row['Due Date'] != 'N/A' else None
                    task = Task(row['Task ID'], row['Title'], row['Description'], due_date, row['Status'])
                    tasks.append(task)
            print("Tasks loaded from tasks.csv successfully!\n")
        except FileNotFoundError:
            print("tasks.csv not found. No tasks loaded.\n")
        return tasks


# JSON implementation
class JSONHandler(FileHandler):
    def save_tasks(self, tasks):
        with open('tasks.json', mode='w') as file:
            # Convert Task objects to dictionaries
            task_list = [
                {
                    'task_id': task.task_id,
                    'title': task.title,
                    'description': task.description,
                    'due_date': task.due_date,
                    'status': task.status
                }
                for task in tasks
            ]
            json.dump(task_list, file, indent=4)
        print("Tasks saved to tasks.json successfully!\n")

    def load_tasks(self):
        tasks = []
        try:
            with open('tasks.json', mode='r') as file:
                task_list = json.load(file)
                for task_data in task_list:
                    task = Task(
                        task_data['task_id'],
                        task_data['title'],
                        task_data['description'],
                        task_data['due_date'],
                        task_data['status']
                    )
                    tasks.append(task)
            print("Tasks loaded from tasks.json successfully!\n")
        except FileNotFoundError:
            print("tasks.json not found. No tasks loaded.\n")
        return tasks



class Task:
    def __init__(self, task_id, title, description, due_date=None, status='Pending'):
        self.task_id = task_id
        self.title = title
        self.description = description
        self.due_date = due_date
        self.status = status   

    def __str__(self):
        return f"{self.task_id}, {self.title}, {self.description}, {self.due_date or 'N/A'}, {self.status}"
    
class TaskManager:
    def __init__(self,file_handler):
        self.tasks=file_handler.load_tasks()
        self.file_handler=file_handler  

# 1. **Add a task**: Allow users to add tasks with the following details:
#    - `Task ID`
#    - `Title`
#    - `Description`
#    - `Due Date` (optional)
#    - `Status` (e.g., Pending, In Progress, Completed)


    # Method to add a task with user input
    def add_task(self):
        print("\n--- Add a New Task ---")
        task_id = input("Enter Task ID: ")
        #  Checking if ID exists in the list. 
        if any(task.task_id == task_id for task in self.tasks):
            print(f"Task with ID '{task_id}' already exists. Please use a different ID.\n")
            return  # Exit the function if ID is already taken
        
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        due_date = input("Enter Due Date (YYYY-MM-DD or press Enter to skip): ") or None
        status = input("Enter Status (Pending/In Progress/Completed): ") or "Pending"
        
        task = Task(task_id, title, description, due_date, status)
        self.tasks.append(task)
        self.file_handler.save_tasks(self.tasks)
        print("Task added successfully!\n")


# 2. **View tasks**: Display all tasks with their details.
    def view_tasks(self):
        if not self.tasks:
            print("No tasks available.")
        else:
            for task in self.tasks:
                print(task)


# 3. **Update a task**: Allow users to modify a task's details using its Task ID.
    def update_task(self):       # Method to update a task with user input
        task_id = input("\nEnter Task ID to update: ")
        for task in self.tasks:
            if task.task_id == task_id:
                print("\n--- Update Task ---")
                task.title = input(f"Enter New Title (or press Enter to keep '{task.title}'): ") or task.title
                task.description = input(f"Enter New Description (or press Enter to keep '{task.description}'): ") or task.description
                task.due_date = input(f"Enter New Due Date (YYYY-MM-DD or press Enter to keep '{task.due_date or 'N/A'}'): ") or task.due_date
                task.status = input(f"Enter New Status (Pending/In Progress/Completed or press Enter to keep '{task.status}'): ") or task.status
                self.file_handler.save_tasks(self.tasks)
                print("Task updated successfully!\n")
                return 
        print("Task not found.\n")     #  Returns if task ID is not found 

# 4. **Delete a task**: Remove a task by its Task ID.
    def delete_task(self):
        task_id = input("\nEnter Task ID to delete: ")
        for task in self.tasks:
            if task.task_id == task_id:
                print("\n--- Delete Task ---")
                self.tasks.remove(task)    #  deleting task by remove() method of lists in python 
                self.file_handler.save_tasks(self.tasks)
                print("Task deleted successfully!\n")
                return
        print("Task not found.\n")

# 5. **Filter tasks**: Filter tasks by status (e.g., Pending or Completed).
    def filter_tasks(self):
        status=input("\nEnter status to filter the tasks: Pending/In Progress/Completed ")
        filtered_tasks=[task for task in self.tasks if task.status.lower()==status.lower()] 
        if not filtered_tasks:
            print(f"No tasks with status '{status}'.\n")   #  The task with some status may not be in the list
        else:
            print("\n--- Filtered Tasks ---")
            for task in filtered_tasks:
                print(task)
        print() 

    def main_menu(self):   #  main menu of the to do tasks
        while True:
            print("""\nWelcome to the To Do tasks application!
            Choose one of the options below to continue: 
            1. Add new task
            2. View all tasks
            3. Update an task's information
            4. Delete a task
            5. Filter tasks by status
            6. Exit """)

            choice = input("Choose an option (1-6): ")

            if choice == "1":
                self.add_task()
            elif choice == "2":
                self.view_tasks()
            elif choice == "3":
                self.update_task()
            elif choice == "4":
                self.delete_task()
            elif choice == "5":
                self.filter_tasks()
            elif choice == "6":
                print("Exiting program.")
                break
            else:
                print("Invalid choice. Please enter a number between 1 and 6.")   #  printing message for exceptions

# Ask user for file format choice
file_format = input("Choose file format (CSV or JSON): ").strip().lower()
if file_format == 'csv':
    handler = CSVHandler()
elif file_format == 'json':
    handler = JSONHandler()
else:
    print("Invalid format choice. Defaulting to CSV.")
    handler = CSVHandler()

# Start Task Manager with the chosen handler
TaskManager(handler).main_menu()
