from marshmallow import pre_dump, pre_load
from app.extensions import ma
from app.models.tasks import StatusEnum


class ReturnTaskSchema(ma.Schema):
    """
        Schema for returning tasks to the frontend
    """
    id = ma.UUID()
    title = ma.Str()
    description = ma.Str()
    due_at = ma.DateTime()
    status = ma.Str()
    created_by = ma.UUID()
    updated_by = ma.UUID()
    
    @pre_dump
    def unpack_enum(self, data, many, **kwargs):
        # unpacks the enum into string representation
        model = data.__dict__
        model["status"] = data.status.value
        return model
        
        
class CreateTaskInputSchema(ma.Schema):
    """
        Schema to validate input for creating a new task
    """
    title = ma.Str(required=True)
    description = ma.Str()
    due_at = ma.DateTime(required=True)
    status = ma.Str()
    user_id = ma.UUID(required=True)
    
    @pre_load
    def pack_enum(self, data, many, **kwargs):
        # packs string into enum
        model = data
        model["status"] = StatusEnum(model["status"]).name
        return model