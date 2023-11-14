from app import models
from app.extensions import db
from typing import Optional, List, Union
from datetime import datetime
from uuid import UUID
from app.models.tasks import Task, StatusEnum
from app.models.users import User
import enum
from app.exceptions.tasks import TaskNotFoundException
from sqlalchemy import and_, extract

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
        
        
    def update_task(
        self,
        id: UUID,
        title: str,
        description: Optional[str],
        due_at: datetime,
        status: StatusEnum,
        user_id: UUID
    ) -> Task:
        """
        Updates task given id and passed data
        """
        task = self.get_task_by_id(id)
        task.title = title
        task.description = description
        task.due_at = due_at
        task.status = status
        task.updated_by = user_id
        db.session.add(task)
        db.session.commit()
        return task
        
        
    def delete_task(self, id: UUID):
        task = self.get_task_by_id(id)
        db.session.delete(task)
        db.session.commit()
        
    def get_all(self) -> [Task]:
        tasks = models.Task.query.all()
        return tasks
    
    def get_by_filters(self, due_at: datetime, status: StatusEnum, created_by: UUID, updated_by: UUID) -> [Task]:        
        filters = []
        if due_at:
            # Extract year, month, and day from the due_at datetime
            due_date = due_at.date()
            year = extract('year', models.Task.due_at)
            month = extract('month', models.Task.due_at)
            day = extract('day', models.Task.due_at)

            # Compare only date, month, and year ignoring time
            filters.append(and_(year==due_date.year, month==due_date.month, day==due_date.day))
        if status:
            filters.append(models.Task.status==status)
        if created_by:
            filters.append(models.Task.created_by==created_by)
        if updated_by:
            filters.append(models.Task.updated_by==updated_by)
        tasks = db.session.query(Task).filter(*filters).all()
        return tasks
        
    def get_task_by_id(self, id: UUID):
        task = models.Task.query.get(id)
        if task is None:
            raise TaskNotFoundException(id)
        return task

    # def get_tasks_by_parameters():