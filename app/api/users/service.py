from app.api.users.repository import UserRepository
from app.exceptions.users import UserNotFoundException
from uuid import UUID
from app.models.users import User

class UserService:
    def __init__(self):
        self.repository = UserRepository()
        
    
    def get_by_id(self, id: UUID) -> User:
        """
        Gets user based on passed user id

        Args:
            id (UUID): id of user we would like to retrieve

        Returns:
            User: User with the given id
        """
        user = self.repository.get_by_id(id)

        return user