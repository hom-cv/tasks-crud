from flask import jsonify

# Create a dictionary with validation error messages
def validation_error_handler(err):
    validation_errors = {}
    for field, errors in err.messages.items():
        validation_errors[field] = errors
    return {"error": "Validation failed", "validation_errors": validation_errors}