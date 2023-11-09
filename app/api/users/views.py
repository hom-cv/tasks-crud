from flask import Blueprint, jsonify
from app import models
from app.api.users.schemas import GetUserSchema

blueprint = Blueprint('user', __name__, url_prefix="/user")

"""
    Test endpoint for getting all users
"""
@blueprint.route("", methods=['GET'])
def get_all_users():
    users = models.User.query.all()
    return jsonify(GetUserSchema().dump(users, many=True))