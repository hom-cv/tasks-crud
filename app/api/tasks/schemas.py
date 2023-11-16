from marshmallow import pre_dump, pre_load
from app.extensions import ma
from app.models.tasks import StatusEnum
from marshmallow import ValidationError


class ReturnTaskSchema(ma.Schema):
    """
    Schema for returning tasks to the frontend
    """
    id = ma.UUID()
    title = ma.Str(required=True)
    description = ma.Str(required=True)
    due_at = ma.DateTime(
        format="%m/%d/%Y",
        description="Valid format MM/DD/YYYY",
        required=True,
        allow_none=False
    )
    status = ma.Str(required=True)
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
    description = ma.Str(required=True)
    due_at = ma.DateTime(
        format="%m/%d/%Y",
        description="Valid format MM/DD/YYYY",
        required=True,
        allow_none=False
    )
    status = ma.Str(required=True)
    user_id = ma.UUID(required=True)
    
    @pre_load
    def pack_enum(self, data, many, **kwargs):
        # packs string into enum
        model = data
        model["status"] = StatusEnum(model["status"]).name
        if model["status"] == None:
            raise ValidationError("Not a valid status")
        return model

class UpdateTaskInputSchema(ma.Schema):
    """
    Schema to validate input for updating a task
    """
    title = ma.Str(required=True)
    description = ma.Str(required=True)
    due_at = ma.DateTime(
        format="%m/%d/%Y",
        description="Valid format MM/DD/YYYY",
        required=True,
        allow_none=False
    )
    status = ma.Str(required=True)
    user_id = ma.UUID(required=True)
    
    @pre_load
    def pack_enum(self, data, many, **kwargs):
        # packs string into enum
        model = data
        model["status"] = StatusEnum(model["status"]).name
        if model["status"] == None:
            raise ValidationError("Not a valid status")
        return model
    
class TaskFiltersSchema(ma.Schema):
    due_at = ma.DateTime(
        format="%m/%d/%Y",
        description="Valid format MM/DD/YYYY",
    )
    status = ma.Str()
    created_by = ma.UUID()
    updated_by = ma.UUID()

    @pre_load
    def pack_enum(self, data, many, **kwargs):
        # packs string into enum
        model = data.copy()
        if "status" in model:
            model["status"] = StatusEnum(model["status"]).name
            if model["status"] == None:
                raise ValidationError("Not a valid status")
        return model