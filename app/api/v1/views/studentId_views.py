import json

from flask import request, jsonify, make_response
from flask_jwt_extended import jwt_required
from flask_restful import Resource

from app.api.v1.models.studentId_model import StudentIdModel


class StudentId(Resource):

    @jwt_required
    def post(self):
        """Add a new Id."""

        details = request.get_json()

        surname = details['surname']
        first_name = details['first_name']
        last_name = details['last_name']
        admission_no = details['admission_no']
        subjects = details['subjects']

        studentId = StudentIdModel().save(surname, first_name, last_name, admission_no, subjects)
        return make_response(jsonify({
            "message": "Id assigned successfully"
        }), 201)


class GetId(Resource):

    @jwt_required
    def get(self):
        """View id credentials."""

        empty_list = {}
        studentId = StudentIdModel().get_id()
        studentId = json.loads(studentId)
        if studentId:
            return make_response(jsonify({
                "message": "Retrieved successfully",
                "StudentId": studentId
            }), 200)
        return make_response(jsonify({
            "message": "success",
            "Books": empty_list
        }), 200)
