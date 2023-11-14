class TaskNotFoundException(Exception):
    def __init__(self, task_id):
        self.task_id = task_id
        super().__init__(f"Task with ID {task_id} not found.")