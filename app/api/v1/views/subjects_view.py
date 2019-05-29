import json

from flask import make_response, jsonify, request
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.api.v1.models.subject_model import SubjectsModel


class Subjects(Resource):
    """Creates a new order."""

    @jwt_required
    def post(self):
        """Create a new exam entry."""
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

        res = SubjectsModel().save(admission_no,
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
        return make_response(jsonify({
            "status": "201",
            "message": "Subjects registered successfully!",
            "subjects": res
        }), 201)

    @jwt_required
    def get(self):
        """Fetch all registered subjects."""
        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "subjects": json.loads(SubjectsModel().get_subjects())
        }), 200)


class OneSubject(Resource):
    """Fetch a specific subject."""

    @jwt_required
    def get(self, admission_no):
        """Fetch one subject."""
        subject = SubjectsModel().get_admission_no(admission_no)
        subject = json.loads(subject)
        if subject:
            return make_response(jsonify({
                "status": "200",
                "message": "success",
                "subject": subject
            }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "Exam Not Found"
        }), 404)