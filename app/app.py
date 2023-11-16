"""
    Main app file, contains constructor as well as configures all the 
    required extensions for the app (i.e. ORM, models, routes)
"""
from flask import Flask
from app.extensions import db, migrate
from app import models
from app.api import (
    users,
    tasks
)

def create_app() -> Flask:
    app = Flask(__name__)
    app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://strike:social@database:5432/tasks"

    configure_extensions(app)
    register_routes(app)
    configure_blueprints(app)

    with app.app_context():
        db.create_all()
    
    return app

def configure_extensions(app):
    db.init_app(app)
    migrate.init_app(app, db)

def register_routes(app):
    @app.route("/ping")
    def ping() -> str:
        return "pong"

def configure_blueprints(app):
    app.register_blueprint(users.views.blueprint)
    app.register_blueprint(tasks.views.blueprint)