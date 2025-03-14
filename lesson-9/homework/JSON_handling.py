# ### **Task 3: JSON Handling**

# #### **Load and Save Tasks (JSON)**
# 1. Create a JSON file named `tasks.json` with the following structure:
#    ```json
#    [
#        {"id": 1, "task": "Do laundry", "completed": false, "priority": 3},
#        {"id": 2, "task": "Buy groceries", "completed": true, "priority": 2},
#        {"id": 3, "task": "Finish homework", "completed": false, "priority": 1}
#    ]
#    ```
# 2. Write a Python program to:
#    - Load the tasks from `tasks.json`.
#    - Display all tasks with the following fields: ID, Task Name, Completed Status, Priority.
#    - Save any changes back to the `tasks.json` file (e.g., after modifying a task).

# #### **Calculate Task Completion Stats**
# 1. Write a Python function to calculate the following statistics:
#    - **Total tasks**: Count the total number of tasks.
#    - **Completed tasks**: Count the number of completed tasks.
#    - **Pending tasks**: Count the number of tasks that are not completed.
#    - **Average priority**: Calculate the average priority level of all tasks.
   
#    Display these statistics after loading the tasks.

# #### **Convert JSON Data to CSV**
# 1. Write a function to convert the task data in `tasks.json` to a CSV file named `tasks.csv`. The CSV should have the following columns:
#    - ID
#    - Task Name
#    - Completed Status
#    - Priority

#    For example:
#    ```csv
#    ID,Task,Completed,Priority
#    1,Do laundry,False,3
#    2,Buy groceries,True,2
#    3,Finish homework,False,1
#    ```


import json
import csv

def load_tasks(filename="tasks.json"):
    """Load tasks from a JSON file."""
    try:
        with open(filename, "r") as file:
            return json.load(file)
    except FileNotFoundError:
        print("File not found. Creating a new task list.")
        return []

def save_tasks(tasks, filename="tasks.json"):
    """Save tasks to a JSON file."""
    with open(filename, "w") as file:
        json.dump(tasks, file, indent=4)

def display_tasks(tasks):
    """Display tasks with ID, Task Name, Completed Status, and Priority."""
    print("\nTask List:")
    print("ID | Task Name          | Completed | Priority")
    print("-" * 50)
    for task in tasks:
        print(f"{task['id']:2} | {task['task']:18} | {task['completed']}  | {task['priority']}")

def calculate_statistics(tasks):
    """Calculate task completion stats."""
    total_tasks = len(tasks)
    completed_tasks = sum(1 for task in tasks if task["completed"])
    pending_tasks = total_tasks - completed_tasks
    avg_priority = sum(task["priority"] for task in tasks) / total_tasks if total_tasks else 0
    
    print("\nTask Statistics:")
    print(f"Total tasks: {total_tasks}")
    print(f"Completed tasks: {completed_tasks}")
    print(f"Pending tasks: {pending_tasks}")
    print(f"Average priority: {avg_priority:.2f}")

def convert_json_to_csv(json_filename="tasks.json", csv_filename="tasks.csv"):
    """Convert tasks JSON to CSV format."""
    tasks = load_tasks(json_filename)
    
    with open(csv_filename, "w", newline="") as csvfile:
        fieldnames = ["ID", "Task", "Completed", "Priority"]
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for task in tasks:
            writer.writerow({
                "ID": task["id"],
                "Task": task["task"],
                "Completed": task["completed"],
                "Priority": task["priority"]
            })
    print(f"Tasks successfully saved to {csv_filename}")

# Load tasks
tasks = load_tasks()

# Display tasks
display_tasks(tasks)

# Calculate statistics
calculate_statistics(tasks)

# Convert JSON to CSV
convert_json_to_csv()
