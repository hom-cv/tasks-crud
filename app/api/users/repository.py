from app.extensions import db
from app import models
import uuid

class UserRepository:
    def get_by_id(self, id: uuid):
        user = models.User.query.get(id)
        print("123")
        print(user)
        return user