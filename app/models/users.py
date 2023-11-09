"""
    Model for the User table
    has rows:
        name - name of user : String, required
"""
from app.extensions import db
from app.models.tasks import Task
from sqlalchemy.dialects.postgresql import UUID
import uuid

class User(db.Model):
    __tablename__ = "user"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    name = db.Column(db.String(100), nullable=False)

    created_by_user = db.relationship("Task", uselist=True, back_populates="created_user", foreign_keys=[Task.created_by])
    updated_by_user = db.relationship("Task", uselist=True, back_populates="updated_user", foreign_keys=[Task.updated_by])

    def __init__(self, **kwargs):
        super(User, self).__init__(**kwargs)