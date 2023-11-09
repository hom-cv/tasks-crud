from app import models
from app.extensions import db
from typing import Optional, List, Union
from datetime import datetime
from uuid import UUID
from app.models.tasks import Task, StatusEnum
from app.models.users import User
import enum

class TaskRepository:
    """
        Task Repository which is used to handle all data access with the database.
        Abstracted from service layer in case user ever needs to change database driver
    """

    def create_task(
        self,
        title: str,
        description: Optional[str],
        due_at: datetime,
        status: StatusEnum,
        user: User
    ) -> Task:
        """
            Creates task given the passed data
        """
        task = Task(
            title=title,
            description=description,
            due_at=due_at,
            status=status,
            created_by=user.id,
            updated_by=user.id
        )
        db.session.add(task)
        db.session.commit()
        return task
        
        
    # def update_task():
        
    # def delete_task():
        
    def get_all(self):
        tasks = models.Task.query.all()
        return tasks
        
    # def get_task_by_id():
        
    # def get_tasks_by_parameters():