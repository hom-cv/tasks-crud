from app.api.tasks.repository import TaskRepository
from app.models import Task
from app.models.tasks import StatusEnum
import uuid
import datetime
from typing import Optional
from datetime import datetime
from app.models.tasks import Task, StatusEnum
import enum
from app.api.users.service import UserService

class TaskService:
    
    def __init__(self):
        self.repository = TaskRepository()
    
    def create_task(self,
        title: str,
        description: Optional[str],
        due_at: datetime,
        status: StatusEnum,
        user_id: uuid
    ) -> Task:
        user = UserService().get_by_id(user_id)
        task = self.repository.create_task(
            title=title,
            description=description,
            due_at=due_at,
            status=status,
            user=user
        )
        return task
    
    def get_all_tasks(self):
        all_tasks = self.repository.get_all()
        return all_tasks