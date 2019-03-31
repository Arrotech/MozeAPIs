import json

from flask import make_response, jsonify, request
from flask_restful import Resource

from app.api.v1.models.fees_models import FeesModels

"""from utils.utils import raise_error, check_order_keys"""
from flask_jwt_extended import jwt_required


class Fees(Resource):

    @jwt_required
    def post(self):
        """Accountant can create a new fee entry"""

        details = request.get_json()
        fees = details['Fees']
        fee_paid = details['fee_paid']
        fee_balance = details['fee_balance']

        """if EvaluationModels().get_name(name):
            return {"message": "Already evaluated"}"""

        resp = FeesModels().save(fees, fee_paid, fee_balance)
        return make_response(jsonify({
            "message": "Entry made successsfully"
        }), 201)


class GetFees(Resource):

    @jwt_required
    def get(self):
        """The students, staff and parents can view the fee balance."""

        empty_fees = {}
        fees = FeesModels().get_all_fees()
        fees = json.loads(fees)
        if fees:
            return make_response(jsonify({
                "message": "successfully retrieved"
            }), 200)
        return make_response(jsonify({
            "message": "success",
            "commemts": empty_fees
        }), 200)


class GetFee(Resource):

    @jwt_required
    def get(self, fee_id):
        """The students, staff and parents can view a single comment."""

        fee = FeesModels().get_one_fee(fee_id)
        fee = json.loads(fee)
        if fee:
            return make_response(jsonify({
                "message": "successfully retrieved",
                "Exam": fee
            }), 200)
        return make_response(jsonify({
            "message": "Fees Not Found"
        }), 404)
