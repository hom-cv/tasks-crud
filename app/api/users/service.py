from app.api.users.repository import UserRepository
import uuid

class UserService:
    def __init__(self):
        self.repository = UserRepository()
        
    def get_by_id(self, id: uuid):
        return self.repository.get_by_id(id)