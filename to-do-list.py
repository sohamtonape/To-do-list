# Global list to hold tasks
todo_list = []

# Function to add a task
def add_task(task_name):
    task = {"name": task_name, "completed": False}
    todo_list.append(task)
    print(f"Task '{task_name}' added.")

# Function to delete a task
def delete_task(task_name):
    global todo_list
    todo_list = [task for task in todo_list if task["name"] != task_name]
    print(f"Task '{task_name}' deleted.")

# Function to display tasks
def display_tasks():
    if not todo_list:
        print("No tasks in the list.")
        return
    for task in todo_list:
        status = "Done" if task["completed"] else "Pending"
        print(f"{task['name']} - [{status}]")

# Function to mark a task as complete
def mark_task_complete(task_name):
    for task in todo_list:
        if task["name"] == task_name:
            task["completed"] = True
            print(f"Task '{task_name}' marked as complete.")
            return
    print(f"Task '{task_name}' not found.")

# Function to interact with the to-do list
def todo_list_app():
    while True:
        print("\nTo-Do List Application")
        print("1. Add a task")
        print("2. Delete a task")
        print("3. Display all tasks")
        print("4. Mark a task as complete")
        print("5. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            task_name = input("Enter the task name: ")
            add_task(task_name)
        elif choice == "2":
            task_name = input("Enter the task name to delete: ")
            delete_task(task_name)
        elif choice == "3":
            display_tasks()
        elif choice == "4":
            task_name = input("Enter the task name to mark as complete: ")
            mark_task_complete(task_name)
        elif choice == "5":
            print("Exiting To-Do List Application. Goodbye!")
            break
        else:
            print("Invalid choice. Please choose a valid option.")

# Run the to-do list application
todo_list_app()
