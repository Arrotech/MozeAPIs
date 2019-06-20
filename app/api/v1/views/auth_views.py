import json
from flask import make_response, jsonify, request, Blueprint
from flask_jwt_extended import create_access_token, jwt_required
from app.api.v1.models.users_model import UsersModel
from utils.authorization import admin_required
from utils.utils import is_valid_email, raise_error, check_register_keys, form_restrictions

auth_v1 = Blueprint('auth_v1', __name__)


@auth_v1.route('/register', methods=['POST'])
def signup():
    """A new user can create a new account."""
    errors = check_register_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
    firstname = details['firstname']
    lastname = details['lastname']
    surname = details['surname']
    admission_no = details['admission_no']
    email = details['email']
    password = details['password']
    form = details['form']
    role = details['role']
    if details['firstname'].isalpha() is False:
        return raise_error(400, "firstname is in wrong format")
    if details['lastname'].isalpha() is False:
        return raise_error(400, "lastname is in wrong format")
    if details['surname'].isalpha() is False:
        return raise_error(400, "surname is in wrong format")
    if details['role'].isalpha() is False:
        return raise_error(400, "role is in wrong format")
    if not is_valid_email(email):
        return raise_error(400, "Invalid Email Format!")
    if len(details['password']) < 8:
        return raise_error(400, "length of password should be atleast eight characters")
    user_admission_no = json.loads(UsersModel().get_admission_no(admission_no))
    if user_admission_no:
        return raise_error(400, "Admission Number Already Exists!")
    user_email = json.loads(UsersModel().get_email(email))
    if user_email:
        return raise_error(400, "Email Already Exists!")
    if (form_restrictions(form) is False):
        return raise_error(400, "Form should be 1, 2, 3 or 4")
    user = json.loads(UsersModel(firstname, lastname, surname, admission_no, email, password, form, role).save())
    return make_response(jsonify({
        "message": "Account created successfully!",
        "status": "201",
        "user": user
    }), 201)

@auth_v1.route('/login', methods=['POST'])
def login():
    """Already existing user can sign in to their account."""
    details = request.get_json()
    email = details['email']
    password = details['password']
    user = json.loads(UsersModel().get_email(email))
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
    """An admin can fetch all users."""
    users = json.loads(UsersModel().get_users())
    return make_response(jsonify({
        "status": "200",
        "message": "successfully retrieved",
        "Users": users
    }), 200)

@auth_v1.route('/users/<string:admission_no>', methods=['GET'])
@jwt_required
@admin_required
def get_user(admission_no):
    """An admin can fetch a single user."""
    user = json.loads(UsersModel().get_admission_no(admission_no))
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
