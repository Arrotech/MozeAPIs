import json

from flask import make_response, jsonify, request
from flask_restful import Resource

from app.api.v1.models.evaluation_model import EvaluationModels

"""from utils.utils import raise_error, check_order_keys"""
from flask_jwt_extended import jwt_required


class EvaluateTeachers(Resource):

    @jwt_required
    def post(self):
        """Students can evaluate their teachers."""

        details = request.get_json()
        name = details['name']
        subject = details['subject']
        attendance = details['attendance']
        homework = details['homework']
        rate = details['rate']
        comment = details['comment']

        if EvaluationModels().get_name(name):
            return {"message": "Already evaluated"}

        resp = EvaluationModels().save(name, subject, attendance, homework, rate, comment)
        return make_response(jsonify({
            "message": "Entry made successsfully"
        }), 201)


class GetAllComments(Resource):

    @jwt_required
    def get(self):
        """The leadership can view the evaluation."""

        empty_comments = {}
        comments = EvaluationModels().get_all_comments()
        comments = json.loads(comments)
        if commemts:
            return make_response(jsonify({
                "message": "successfully retrieved"
            }), 200)
        return make_response(jsonify({
            "message": "success",
            "commemts": empty_comments
        }), 200)


class GetOneComment(Resource):

    @jwt_required
    def get(self, comment_id):
        """The leadership can view a single comment."""

        comment = EvaluationModels().get_one_comment(comment_id)
        comment = json.loads(comment)
        if comment:
            return make_response(jsonify({
                "message": "successfully retrieved",
                "Exam": comment
            }), 200)
        return make_response(jsonify({
            "message": "Comment Not Found"
        }), 404)
