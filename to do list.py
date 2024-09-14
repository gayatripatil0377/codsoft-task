import os

TASKS_FILE = 'tasks.txt'

def load_tasks():
    """Load tasks from the file."""
    if not os.path.exists(TASKS_FILE):
        return []
    
    with open(TASKS_FILE, 'r') as file:
        tasks = file.readlines()
    return [task.strip() for task in tasks]

def save_tasks(tasks):
    """Save tasks to the file."""
    with open(TASKS_FILE, 'w') as file:
        for task in tasks:
            file.write(f"{task}\n")

def display_tasks(tasks):
    """Display the list of tasks."""
    if not tasks:
        print("No tasks found.")
    else:
        print("Your tasks:")
        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

def add_task(tasks):
    """Add a new task to the list."""
    task = input("Enter the new task: ")
    tasks.append(task)
    print(f"Task '{task}' added.")

def remove_task(tasks):
    """Remove a task from the list."""
    display_tasks(tasks)
    try:
        index = int(input("Enter the number of the task to remove: ")) - 1
        if 0 <= index < len(tasks):
            removed_task = tasks.pop(index)
            print(f"Task '{removed_task}' removed.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Invalid input. Please enter a number.")

def main():
    tasks = load_tasks()
    
    while True:
        print("\nTo-Do List Menu:")
        print("1. View tasks")
        print("2. Add task")
        print("3. Remove task")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
            save_tasks(tasks)
        elif choice == '3':
            remove_task(tasks)
            save_tasks(tasks)
        elif choice == '4':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
