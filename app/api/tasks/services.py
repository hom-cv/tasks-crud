from app.api.tasks.repository import TaskRepository
from app.models import Task
from app.models.tasks import StatusEnum
from uuid import UUID
import datetime
from typing import Optional
from datetime import datetime
from app.models.tasks import Task, StatusEnum
import enum
from app.api.users.service import UserService

class TaskService:
    
    def __init__(self):
        """
            Initiates task respository for use within the service
        """
        self.repository = TaskRepository()
    
    def create_task(self,
        title: str,
        due_at: datetime,
        user_id: UUID,
        description: Optional[str] = "",
        status: StatusEnum = "pending"
    ) -> Task:
        """
            Creates a task using the given parameters

            Args:
                title (str): title of the task
                due_at (datetime): due date of the task in ISO 8601 format
                user_id (UUID): UUID of the user creating the task
                description (Optional[str], optional): description associated with the task. Defaults to "".
                status (StatusEnum, optional): status of the task, has to be one of the available enums in StatusEnum. Defaults to "pending".

            Returns:
                Task: returns the task created from the endpoint
        """
        user = UserService().get_by_id(user_id)
        task = self.repository.create_task(
            title=title,
            description=description,
            due_at=due_at,
            status=status,
            user=user
        )
        return task
    
    def get_all_tasks(self) -> [Task]:
        """
            Gets all available tasks from the database

            Returns:
                [Task]: returns an array of all the Tasks
        """
        all_tasks = self.repository.get_all()
        return all_tasks
    
    def get_task_by_id(self, id: UUID) -> Task:
        """
            Gets a task with the matching passed id

            Args:
                id (UUID): id of the task that is to be fetched

            Returns:
                Task: returns the Task associated with the passed id
        """
        task = self.repository.get_task_by_id(id)
        return task
    
    def get_task_by_filter(self, due_at=None, status=None, created_by=None, updated_by=None) -> [Task]:
        """
            Gets all the tasks with the appropriate filters

            Args:
                due_at (_type_, optional): due date of the task that we want to fetch. Defaults to None.
                status (_type_, optional): status of the task that we want to fetch. Defaults to None.
                created_by (_type_, optional): user_id of the creator of the task that we want to fetch. Defaults to None.
                updated_by (_type_, optional): ser_id of the last editor of the task that we want to fetch. Defaults to None.

            Returns:
                [Task]: returns an array of all the Tasks that matches the applied filters
        """
        filtered_tasks = self.repository.get_by_filters(
            due_at,
            status,
            created_by,
            updated_by
        )
        return filtered_tasks
    
    def update_task_by_id(
        self,
        id: UUID,
        title: str,
        due_at: datetime,
        user_id: UUID,
        status: StatusEnum,
        description: Optional[str] = ""
    ) -> Task:
        """
            Updates a task of the given id with the new passed data

            Args:
                id (UUID): id of the task we want to update
                title (str): new title that we would like to apply to the task
                due_at (datetime): new due date that we would like to apply to the task
                user_id (UUID): user editing the task
                status (StatusEnum): new status that we would like to apply to the task
                description (Optional[str], optional): new description that we would like to apply to the task. Defaults to "".

            Returns:
                Task: returns the newly created Task
        """
        user_service = UserService()
        # makes sure user exists
        user = user_service.get_by_id(user_id)
        task = self.repository.update_task(id=id, title=title, description=description, due_at=due_at, user_id=user_id, status=status)
        return task
    
    def delete_task_by_id(
        self,
        id: UUID
    ):
        """
            Deletes task which has the given id

            Args:
                id (UUID): id of the task we would like to delete
        """
        task = self.repository.delete_task(id=id)