from functools import wraps
from flask import jsonify, request
from app.models import Program


def token_required(a_function):
    @wraps(a_function)
    def decorated_function(*args, **kwargs):
        token = request.headers.get('x-access-token') # get the API token provided by the user or get None
        #if no token - stop and tell them
        if not token:
            return jsonify({'Access Denied': 'No API token provies - please register to use create, update, delete routes (CUD)'})
        # if not valid token stop them and tell them
        u = Program.query.filter_by(apitoken= token).first()
        if not u:
            return jsonify({'Access denied': 'invalid API token - please register to use CUD routes '})
        # if yees valid- let them continue
        return a_function(*args, **kwargs)
    return decorated_function