from app.extensions import db
from app import models
from uuid import UUID
from exceptions.users import UserNotFoundException

class UserRepository:
    """
        User Repository which is used to handle all data access with the database.
        Abstracted from service layer in case user ever needs to change database driver
    """
    def get_by_id(self, id: UUID):
        user = models.User.query.get(id)
        if not user:
            raise UserNotFoundException(id)
        return user