"""Json package."""
import json

from flask import make_response, jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.api.v1.models.exams_model import ExamsModel
from utils.authorization import admin_required
from utils.utils import check_exams_keys

exams_v1 = Blueprint('exams_v1', __name__)

@exams_v1.route('/exams', methods=['POST'])
@jwt_required
@admin_required
def add_exam():
    """Create a new exam entry."""
    errors = check_exams_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
    admission_no = details['admission_no']
    maths = details['maths']
    english = details['english']
    kiswahili = details['kiswahili']
    chemistry = details['chemistry']
    biology = details['biology']
    physics = details['physics']
    history = details['history']
    geography = details['geography']
    cre = details['cre']
    agriculture = details['agriculture']
    business = details['business']

    exam = ExamsModel().save(admission_no,
                             maths,
                             english,
                             kiswahili,
                             chemistry,
                             biology,
                             physics,
                             history,
                             geography,
                             cre,
                             agriculture,
                             business)
    exam = json.loads(exam)
    return make_response(jsonify({
        "status": "201",
        "message": "Entry created successfully!",
        "exams": exam
    }), 201)

@exams_v1.route('/exams', methods=['GET'])
@jwt_required
def get_exams():
    """Get all exams."""
    return make_response(jsonify({
        "status": "200",
        "message": "successfully retrieved",
        "exams": json.loads(ExamsModel().get_all_exams())
    }), 200)

@exams_v1.route('/exams/<int:exam_id>', methods=['GET'])
@jwt_required
def get_exam(exam_id):
    """Fetch one exam."""
    exam = ExamsModel().get_exam_by_id(exam_id)
    exam = json.loads(exam)
    if exam:
        return make_response(jsonify({
            "status": "200",
            "message": "successfully retrieved",
            "Exam": exam
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "Exam Not Found"
    }), 404)

@exams_v1.route('/exams/<int:exam_id>', methods=['PUT'])
@jwt_required
@admin_required
def put(exam_id):
    """Update exams scores."""
    details = request.get_json()
    admission_no = details['admission_no']
    maths = details['maths']
    english = details['english']
    kiswahili = details['kiswahili']
    chemistry = details['chemistry']
    biology = details['biology']
    physics = details['physics']
    history = details['history']
    geography = details['geography']
    cre = details['cre']
    agriculture = details['agriculture']
    business = details['business']

    exam = ExamsModel().update_scores(admission_no,
                                      maths,
                                      english,
                                      kiswahili,
                                      chemistry,
                                      biology,
                                      physics,
                                      history,
                                      geography,
                                      cre,
                                      agriculture,
                                      business,
                                      exam_id)
    exam = json.loads(exam)
    if exam:
        return make_response(jsonify({
            "status": "200",
            "message": "Scores successfully updated",
            "exam": exam
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "Exam not found!"
    }), 404)

@exams_v1.route('/exams/<int:exam_id>', methods=['DELETE'])
@jwt_required
@admin_required
def delete(exam_id):
    """Delete a specific exam."""
    exam = ExamsModel().get_exam_by_id(exam_id)
    exam = json.loads(exam)
    if exam:
        ExamsModel().delete_exam(exam_id)
        return make_response(jsonify({
            "status": "200",
            "message": "Exam deleted successfully"
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "Exam not found"
    }), 404)
