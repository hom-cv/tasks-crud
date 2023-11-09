from app.extensions import ma

"""
    Schema for returning users when getting from database
"""
class GetUserSchema(ma.Schema):
    id = ma.UUID()
    name = ma.Str()