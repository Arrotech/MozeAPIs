"""Import flask module."""
from flask import Flask, jsonify, make_response
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from flask_restful import Api

from app.api.v1.views.auth_views import SignIn, CreateAccount, User, Users
from app.api.v1.views.evaluation_views import EvaluateTeachers, GetAllComments, GetOneComment
from app.api.v1.views.exam_views import Exams, OneExam
from app.api.v1.views.fees_views import Fees, GetFees, GetFee
from app.api.v1.views.library_views import Library, GetBooks, GetOneBook
from app.api.v1.views.studentId_views import StudentId, GetId
from app.api.v1.views.subjects_view import Subjects, GetAllSubjects
from app.config import app_config


def page_not_found(e):
    """Capture Not Found error."""
    return make_response(jsonify({
        "status": "400",
        "message": "resource not found"
    }), 404)


def method_not_allowed(e):
    """Capture Not Found error."""
    return make_response(jsonify({
        "status": "405",
        "message": "method not allowed"
    }), 405)


def bad_request(e):
    """Capture Not Found error."""
    return make_response(jsonify({
        "status": "400",
        "message": "bad request"
    }), 400)


def internal_server_error(e):
    """Capture Not Found error."""
    return make_response(jsonify({
        "status": "500",
        "message": "internal server error"
    }), 500)


def exam_app(config_name):
    """Create the app."""
    app = Flask(__name__)
    CORS(app)

    app.config.from_pyfile('config.py')
    app.config["SECRET_KEY"] = 'thisisarrotech'
    jwt = JWTManager(app)

    api = Api(app)

    api.add_resource(CreateAccount, '/api/v1/portal/auth/register')
    api.add_resource(SignIn, '/api/v1/portal/auth/login')
    api.add_resource(Exams, '/api/v1/portal/exams')
    api.add_resource(OneExam, '/api/v1/portal/exams/<string:admission_no>')
    api.add_resource(User, '/api/v1/portal/user/<int:user_id>')
    api.add_resource(Users, '/api/v1/portal/users')
    api.add_resource(EvaluateTeachers, '/api/v1/portal/evaluate')
    api.add_resource(GetAllComments, '/api/v1/portal/evaluate')
    api.add_resource(GetOneComment, '/api/v1/portal/evaluate/<int:comment_id>')
    api.add_resource(Fees, '/api/v1/portal/fees')
    api.add_resource(GetFees, '/api/v1/portal/fees')
    api.add_resource(GetFee, '/api/v1/portal/fees/<int:fee_id>')
    api.add_resource(Library, '/api/v1/portal/library')
    api.add_resource(GetBooks, '/api/v1/portal/library')
    api.add_resource(GetOneBook, '/api/v1/portal/library/<int:book_id>')
    api.add_resource(Subjects, '/api/v1/portal/subjects')
    api.add_resource(GetAllSubjects, '/api/v1/portal/subjects')
    api.add_resource(StudentId, '/api/v1/portal/id')
    api.add_resource(GetId, '/api/v1/portal/id')
    app.register_error_handler(404, page_not_found)
    app.register_error_handler(405, method_not_allowed)
    app.register_error_handler(400, bad_request)
    app.register_error_handler(500, internal_server_error)

    return app
