from flask import jsonify
from flask_restful import abort
from webargs.flaskparser import parser
from new_app import myapp

@myapp.errorhandler(404)
def handle_exception(err):
    """Return JSON instead of HTML for any other server error"""
    return jsonify({'error': f'{str(err)}'})


@parser.error_handler
def handle_request_parsing_error(err, req, schema, *, error_status_code, error_headers):
    """webargs error handler that uses Flask-RESTful's abort function to return
    a JSON error response to the client.
    """
    abort(error_status_code, errors=err.messages)
