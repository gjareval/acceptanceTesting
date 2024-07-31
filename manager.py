
from task import Task


class ToDoListManager:
    def __init__(self):
        self.tasks = {}
        self.next_id = 1

    def add_task(self, description, due_date):
        task = Task(self.next_id, description, due_date)
        self.tasks[self.next_id] = task
        self.next_id += 1
        print(f"Task added: {task}")

    def list_tasks(self):
        if not self.tasks:
            print("No tasks in the list.")
        else:
            for task in self.tasks.values():
                print(task)

    def mark_task_completed(self, task_id):
        if task_id in self.tasks:
            self.tasks[task_id].mark_completed()
            print(f"Task {task_id} marked as completed.")
        else:
            print(f"No task found with ID {task_id}.")

    def mark_all_tasks_completed(self):
        if not self.tasks:
            print("No tasks to mark as completed.")
        else:
            for task in self.tasks.values():
                task.mark_completed()
            print("All tasks have been marked as completed.")

    def clear_tasks(self):
        self.tasks.clear()
        print("All tasks cleared.")