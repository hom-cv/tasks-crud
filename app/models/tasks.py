"""
    Model for the Task table
    has rows:
        title - title of task : String, required
        description - description of task : String, not required
        due_at - due date of task : DateTime, required
        status - status of task : Enum['COMPLETED', 'IN_PROGRESS', 'PENDING'], required
        created_by - FK User who created the task, required
        updated_by - FK User who most recently updated the task, required
"""
from app.extensions import db
from sqlalchemy.dialects.postgresql import UUID
import uuid
import enum

class StatusEnum(enum.Enum):
    COMPLETED = "completed"
    IN_PROGRESS = "in_progress"
    PENDING = "pending"

class Task(db.Model):
    __tablename__ = "task"

    id = db.Column(
        UUID(as_uuid=True),
        primary_key=True,
        default=uuid.uuid4,
        nullable=False,
        unique=True,
    )
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.String(255), nullable=True)
    due_at = db.Column(db.DateTime(timezone=True), nullable=False)
    status = db.Column(db.Enum(StatusEnum), nullable=False, default=StatusEnum.PENDING)
    created_by = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id", ondelete='SET NULL'), index=True)
    updated_by = db.Column(UUID(as_uuid=True), db.ForeignKey("user.id", ondelete='SET NULL'), index=True)
    created_user = db.relationship("User", uselist=False, back_populates="created_by_user", foreign_keys=[created_by])
    updated_user = db.relationship("User", uselist=False, back_populates="updated_by_user", foreign_keys=[updated_by])


    def __init__(self, **kwargs):
        super(Task, self).__init__(**kwargs)