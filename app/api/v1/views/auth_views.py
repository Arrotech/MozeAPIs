import json

from flask import make_response, jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required
from flask_restful import Resource
from werkzeug.security import generate_password_hash

from app.api.v1.models.users_model import UsersModel
from utils.authorization import admin_required
from utils.utils import is_valid_email, raise_error, check_register_keys, form_restrictions

auth_v1 = Blueprint('auth_v1', __name__)
# auth2_v1 = Blueprint('auth2_v1', __name__)

@auth_v1.route('/register', methods=['POST'])
def signup():
    """A user can create a new account."""
    errors = check_register_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
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

@auth_v1.route('/login', methods=['POST'])
def login():
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

@auth_v1.route('/users', methods=['GET'])
@jwt_required
@admin_required
def get_users():
    return make_response(jsonify({
        "status": "200",
        "message": "successfully retrieved",
        "Users": json.loads(UsersModel().get_users())
    }))

@auth_v1.route('/users/<int:user_id>', methods=['GET'])
@jwt_required
@admin_required
def get_user(user_id):
    """Admin can fetch a single user"""
    user = UsersModel().get_user_by_id(user_id)
    user = json.loads(user)
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
