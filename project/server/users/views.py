from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView

from project.server import bcrypt, db
from project.server.models import User

list_blueprint = Blueprint('users', __name__)

class ListAPI(MethodView):
    '''
    User list resources
    '''

    def get(self):
        result = []
        allUsers = User.query.all()
        for user in allUsers:
            result.append(
                {"admin": user.admin,
                 "email": user.email,
                 "id": user.id,
                 "registered_on": user.registered_on}
            )
        responseObject = {
            'status': 'success',
            'message': 'successfully retrieved all user records',
            'users': result
        }
        return make_response(jsonify(responseObject)), 201



list_view = ListAPI.as_view('list_api')

# add Rules for API endpoints
list_blueprint.add_url_rule(
    '/users/index',
    view_func=list_view,
    methods=['GET']
)