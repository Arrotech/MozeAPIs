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

        res = SubjectsModel().save(maths, english, kiswahili, chemistry, biology, physics, history, geography, cre,
                                   agriculture, business)
        return make_response(jsonify({
            "message": "Subjects registered successfully!"
        }), 201)


class GetAllSubjects(Resource):
    """Fetch all orders."""

    @jwt_required
    def get(self):
        empty_list = {}
        subjects = SubjectsModel().get_all_subjects()
        subjects = json.loads(subjects)
        if subjects:
            return make_response(jsonify({
                "message": "success",
                "Subjects registered": subjects
            }), 200)
        return make_response(jsonify({
            "message": "success",
            "Subjects registered": empty_list
        }), 200)
