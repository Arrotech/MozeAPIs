"""Json package."""
import json

from flask import make_response, jsonify, request, Blueprint
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.api.v1.models.exams_model import ExamsModel
from app.api.v1.models.users_model import UsersModel
from utils.authorization import admin_required
from utils.utils import check_exams_keys, form_restrictions, term_restrictions, type_restrictions

exams_v1 = Blueprint('exams_v1', __name__)

@exams_v1.route('/exams', methods=['POST'])
@jwt_required
@admin_required
def add_exam():
    """Create a new exam entry for an existing user."""
    errors = check_exams_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
    admission_no = details['admission_no']
    term = details['term']
    form = details['form']
    type = details['type']
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
    if (form_restrictions(form) is False):
        return raise_error(400, "Form should be 1, 2, 3 or 4")
    if (term_restrictions(term) is False):
        return raise_error(400, "Term should be either 1st, 2nd, 3rd, 1ST, 2ND, or 3RD")
    if (type_restrictions(type) is False):
        return raise_error(400, "Type should be either MAIN, main, CAT, or cat")
    user = json.loads(UsersModel().get_admission_no(admission_no))
    if user:
        exam = ExamsModel(admission_no,
                          term,
                          form,
                          type,
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
                          business).save()
        exam = json.loads(exam)
        return make_response(jsonify({
            "status": "201",
            "message": "Entry created successfully!",
            "exams": exam
        }), 201)
    return make_response(jsonify({
        "status": "404",
        "message": "Student with that Admission Number does not exitst."
    }), 404)

@exams_v1.route('/exams', methods=['GET'])
@jwt_required
def get_exams():
    """Get all exams entries for all students."""
    return make_response(jsonify({
        "status": "200",
        "message": "successfully retrieved",
        "exams": json.loads(ExamsModel().get_all_exams())
    }), 200)

@exams_v1.route('/exams/<string:admission_no>', methods=['GET'])
@jwt_required
def get_exam(admission_no):
    """Fetch an exam by specific Admission Number."""
    exam = ExamsModel().get_exam_by_admission_no(admission_no)
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

@exams_v1.route('/exams/<string:admission_no>', methods=['PUT'])
@jwt_required
@admin_required
def put(admission_no):
    """Update an exam scores for a specific student by Admission Number."""
    details = request.get_json()
    admission_no = details['admission_no']
    term = details['term']
    form = details['form']
    type = details['type']
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
    exam = ExamsModel(admission_no,
                      term,
                      form,
                      type,
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
                      business).update_scores()
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

@exams_v1.route('/exams/<string:admission_no>', methods=['DELETE'])
@jwt_required
@admin_required
def delete(admission_no):
    """Delete an exam by Admission Number."""
    exam = ExamsModel().get_exam_by_admission_no(admission_no)
    exam = json.loads(exam)
    if exam:
        ExamsModel().delete_exam(admission_no)
        return make_response(jsonify({
            "status": "200",
            "message": "Exam deleted successfully"
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "Exam not found"
    }), 404)
