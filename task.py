class Task:
    def __init__(self, task_id, description):
        self.task_id = task_id
        self.description = description
        self.status = 'Pending'

    def mark_completed(self):
        self.status = 'Completed'

    def __str__(self):
        return f"ID: {self.task_id} | Description: {self.description} | Status: {self.status}"
