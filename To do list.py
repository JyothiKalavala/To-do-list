tasks = []

def display_menu():
    print("\nTo-Do List Menu")
    print("a. Add Tasks")
    print("b. Delete Task")
    print("c. Mark Task as Completed")
    print("d. View Tasks")
    print("e. Exit")

def view_tasks():
    if not tasks:
        print("\nNo tasks available.")
    else:
        print("\nYour Tasks:")
        for i, task in enumerate(tasks, start=1):
            status = "Done" if task["completed"] else "Not Done"
            print(f"{i}. {task['task']} [{status}]")

def add_tasks():
    task_name = input("\nEnter the task: ").strip()
    if task_name:
        tasks.append({"task": task_name, "completed": False})
        print("Task added successfully!")
    else:
        print("Task cannot be empty.")

def mark_task_completed():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to mark as completed: "))
            if 1 <= task_number <= len(tasks):
                tasks[task_number - 1]["completed"] = True
                print("Task marked as completed!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Enter a valid number.")

def delete_task():
    view_tasks()
    if tasks:
        try:
            task_number = int(input("\nEnter the task number to delete: "))
            if 1 <= task_number <= len(tasks):
                deleted_task = tasks.pop(task_number - 1)
                print(f"Task '{deleted_task['task']}' deleted successfully!")
            else:
                print("Invalid task number.")
        except ValueError:
            print("Please enter a valid number.")

def main():
    while True:
        display_menu()
        choice = input("\nEnter your choice (a-e): ").lower().strip()
        if choice == "a":
            add_tasks()
        elif choice == "b":
            delete_task()
        elif choice == "c":
            mark_task_completed()
        elif choice == "d":
            view_tasks()
        elif choice == "e":
            print("Exiting the program. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
    
