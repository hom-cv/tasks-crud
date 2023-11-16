from flask import Blueprint, jsonify, request
from app import models
from app.api.tasks.services import TaskService
from app.api.tasks.schemas import ReturnTaskSchema, CreateTaskInputSchema, UpdateTaskInputSchema, TaskFiltersSchema
from app.exceptions.users import UserNotFoundException
from marshmallow import ValidationError
from app.utils.helpers import validation_error_handler
from app.exceptions.tasks import TaskNotFoundException
from datetime import datetime

blueprint = Blueprint('task', __name__, url_prefix="/task")

"""
    Endpoint for creating a new task
    request_body:
        title: str,
        description: str,
        due_at: datetime, 
        status: ['completed', 'in_progress', 'pending'],
        user_id: uuid
    responses:
        201 - New task created
        404 - User not found
        400 - Validation error
"""
@blueprint.route("", methods=['POST'])
def create_task():
    try:
        request_json = CreateTaskInputSchema().load(request.json)
        service = TaskService()
        task = service.create_task(**request_json)
        return jsonify(ReturnTaskSchema().dump(task)), 201
    except UserNotFoundException as user_not_found:
        return jsonify({"error": str(user_not_found)}), 404
    except ValidationError as err:
        return jsonify(validation_error_handler(err)), 400
    except Exception as err:
        return jsonify({"error": str(err)}), 400

"""
    Endpoint for getting all tasks
    If no URL parameters are passed, gets all tasks, else, gets tasks 
    based on passed due date, status, created_by or updated_by
    
    url_params:
        due_at: date,
        status: ['completed', 'in_progress', 'pending'],
        created_by: uuid,
        updated_by: uuid
    request_body:
        due_at: datetime, 
        status: ['completed', 'in_progress', 'pending'],
        created_by: uuid,
        updated_by: uuid
    responses:
        200 - Tasks retrieved
        404 - User not found
"""
@blueprint.route("", methods=['GET'])
def get_all_tasks():
    try:
        service = TaskService()
        request_args = request.args
        if len(request_args) == 0:
            tasks = service.get_all_tasks()
        else:
            print(request_args)
            task_filters = TaskFiltersSchema().load(request_args)
            tasks = service.get_task_by_filter(**task_filters)
        return jsonify(ReturnTaskSchema().dump(tasks, many=True))
    except Exception as err:
            return jsonify({"error": str(err)}), 400

"""
    Endpoint for getting a task by its id
    query:
        task_id - ID of task that is to be retrieved
    responses:
        201 - New task created
        404 - Task not found
        400 - Validation error
"""
@blueprint.route("/<uuid:task_id>", methods=['GET'])
def get_task_by_id(task_id):
    try:
        service = TaskService()
        task = service.get_task_by_id(id=task_id)
        return jsonify(ReturnTaskSchema().dump(task))
    except TaskNotFoundException as task_not_found:
        return jsonify({"error": str(task_not_found)}), 404
    except Exception as err:
            return jsonify({"error": str(err)}), 400

"""
    Endpoint for updating a task by its id
    query:
        task_id - ID of task that is to be updated
    request_body:
        title: str,
        description: str,
        due_at: datetime, 
        status: ['completed', 'in_progress', 'pending'],
        user_id: uuid
    responses:
        200 - Task updated successfully
        404 - User not found, Task not found
        400 - Validation error
"""
@blueprint.route("/<uuid:task_id>", methods=['PUT'])
def update_task_by_id(task_id):
    try:
        request_json = UpdateTaskInputSchema().load(request.json)
        service = TaskService()
        task = service.update_task_by_id(id=task_id, **request_json)
        return jsonify(ReturnTaskSchema().dump(task))
    except TaskNotFoundException or UserNotFoundException as not_found:
        return jsonify({"error": str(not_found)}), 404
    except Exception as err:
            return jsonify({"error": str(err)}), 400
        
"""
    Endpoint for deleting a task by its id
    query:
        task_id - ID of task that is to be deleted
    responses:
        200 - Task deleted successfully
        404 - Task not found
        400 - Validation error
"""    
@blueprint.route("/<uuid:task_id>", methods=['DELETE'])
def delete_task_by_id(task_id):
    try:
        service = TaskService()
        task = service.delete_task_by_id(id=task_id)
        return jsonify({"message": "Task successfully deleted"}), 200
    except TaskNotFoundException as task_not_found:
        return jsonify({"error": str(task_not_found)}), 404
    except Exception as err:
            return jsonify({"error": str(err)}), 400