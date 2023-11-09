from flask import Blueprint, jsonify, request
from app import models
from app.api.tasks.services import TaskService
from app.api.tasks.schemas import ReturnTaskSchema, CreateTaskInputSchema

blueprint = Blueprint('task', __name__, url_prefix="/task")

"""
    Endpoint for getting all tasks
"""
@blueprint.route("", methods=['POST'])
def create_task():
    request_json = CreateTaskInputSchema().load(request.json)
    service = TaskService()
    task = service.create_task(**request_json)
    return jsonify(ReturnTaskSchema().dump(task))

@blueprint.route("", methods=['GET'])
def get_all_tasks():
    service = TaskService()
    tasks = service.get_all_tasks()
    return jsonify(ReturnTaskSchema().dump(tasks, many=True))

