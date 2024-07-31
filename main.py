
import sys
import datetime
from manager import ToDoListManager


def main():
    manager = ToDoListManager()
    
    while True:
        print("\nTo-Do List Manager")
        print("1. Add a new task")
        print("2. List all tasks")
        print("3. Mark a task as completed")
        print("4. Mark all tasks as completed")
        print("5. Clear the entire to-do list")
        print("6. Exit")
        choice = input("Choose an option: ")

        if choice == '1':
            description = input("Enter task description: ")
            try:
                manager.add_task(description)
            except ValueError:
                print("Invalid date format.")
        
        elif choice == '2':
            manager.list_tasks()
        
        elif choice == '3':
            task_id = int(input("Enter task ID to mark as completed: "))
            manager.mark_task_completed(task_id)

        elif choice == '4':
            manager.mark_all_tasks_completed()
        
        elif choice == '5':
            manager.clear_tasks()
        
        elif choice == '6':
            print("Exiting To-Do List Manager.")
            sys.exit()
        
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
