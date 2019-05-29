import json

from flask import make_response, jsonify, request
from flask_restful import Resource

from app.api.v1.models.fees_models import FeesModels

"""from utils.utils import raise_error, check_order_keys"""
from flask_jwt_extended import jwt_required


class Fees(Resource):
    """School fees."""

    @jwt_required
    def post(self):
        """Accountant can create a new fee entry"""
        details = request.get_json()
        admission_no = details['admission_no']
        transaction_type = details['transaction_type']
        transaction_no = details['transaction_no']
        description = details['description']
        amount = details['amount']

        deposit = FeesModels().save(admission_no,
                                    transaction_type,
                                    transaction_no,
                                    description,
                                    amount)
        deposit = json.loads(deposit)
        return make_response(jsonify({
            "status": "201",
            "message": "Entry made successsfully",
            "deposit": deposit
        }), 201)

    @jwt_required
    def get(self):
        """The students, staff and parents can view the fee balance."""
        return make_response(jsonify({
            "status": "200",
            "message": "successfully retrieved",
            "fees": json.loads(FeesModels().get_all_fees())
        }), 200)


class GetFee(Resource):
    """Individual fees."""

    @jwt_required
    def get(self, admission_no):
        """The students, staff and parents can view a single comment."""
        fee = FeesModels().get_admission_no(admission_no)
        fee = json.loads(fee)
        if fee:
            return make_response(jsonify({
                "status": "200",
                "message": "successfully retrieved",
                "Exam": fee
            }), 200)
        return make_response(jsonify({
            "status": "404",
            "message": "Fees Not Found"
        }), 404)
