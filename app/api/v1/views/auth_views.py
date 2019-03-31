import json

from flask import make_response, jsonify, request
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from app.api.v1.models.users_model import UsersModel
from utils.authorization import admin_required
from utils.utils import is_valid_email, raise_error, check_register_keys, form_restrictions


class CreateAccount(Resource):
    """Create a new account."""

    def post(self):
        """A user can create a new account."""

        details = request.get_json()

        errors = check_register_keys(request)
        if errors:
            return raise_error(400, "Invalid {} key".format(', '.join(errors)))

        firstname = details['firstname']
        lastname = details['lastname']
        surname = details['surname']
        admission_no = details['admission_no']
        email = details['email']
        password = generate_password_hash(details['password'])
        form = details['form']

        if details['firstname'].isalpha() is False:
            return raise_error(400, "firstname is in wrong format")
        if details['lastname'].isalpha() is False:
            return raise_error(400, "lastname is in wrong format")
        if details['surname'].isalpha() is False:
            return raise_error(400, "surname is in wrong format")
        if not is_valid_email(email):
            return raise_error(400, "Invalid Email Format!")
        if UsersModel().get_admission_no(admission_no):
            return raise_error(400, "Admission Number Already Exists!")
        user_email = UsersModel().get_email(email)
        user_email = json.loads(user_email)
        if user_email:
            return raise_error(400, "Email Already Exists!")
        if (form_restrictions(form) is False):
            return raise_error(400, "select from 1, 2, 3 or 4")

        user = UsersModel(firstname, lastname, surname, admission_no, email, password, form).save()
        return make_response(jsonify({
            "message": "Account created successfully!",
            "status": "201",
            "user": json.loads(user)
        }), 201)


class SignIn(Resource):
    """SignIn to the account."""

    def post(self):
        """A user can sign in to their account."""

        details = request.get_json()
        email = details['email']
        password = details['password']

        user = UsersModel().get_email(email)
        user = json.loads(user)
        if user:
            token = create_access_token(identity=email)
            return make_response(jsonify({
                "status": "200",
                "message": "Successfully logged in!",
                "token": token,
                "user": user
            }), 200)
        return make_response(jsonify({
            "status": "401",
            "message": "Invalid Email or Password"
        }), 401)


class User(Resource):
    """Fetch orders by a single user"""


@jwt_required
@admin_required
def get(self, user_id):
    """Admin can fetch a single user"""

    user = UsersModel().get_user_by_id(user_id)
    user = json.loads(user)
    print(user)
    if user:
        return make_response(jsonify({
            "status": "200",
            "message": "successfully retrieved",
            "user": user
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "User Not Found"
    }), 404)


class Users(Resource):
    """Admin can fetch all users"""

    @jwt_required
    @admin_required
    def get(self):
        users = UsersModel().get_users()
        users = json.loads(users)
        if users:
            return make_response(jsonify({
                "status": "200",
                "message": "All users",
                "Users": users
            }))
