class Task:
    def __init__(self, task_id, description, due_date):
        self.task_id = task_id
        self.description = description
        self.due_date = due_date
        self.status = 'Pending'

    def mark_completed(self):
        self.status = 'Completed'

    def __str__(self):
        return f"ID: {self.task_id} | Description: {self.description} | Due Date: {self.due_date} | Status: {self.status}"
