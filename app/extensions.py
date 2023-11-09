"""
    Extensions required for the database
    SQLAlchemy - Database ORM
    Marshmallow - Schema validator
    Migrate - Database migration manager
"""
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_migrate import Migrate

db: SQLAlchemy = SQLAlchemy()
ma: Marshmallow = Marshmallow()
migrate: Migrate = Migrate(compare_type=True)