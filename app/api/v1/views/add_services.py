import json
from flask import make_response, jsonify, request, Blueprint
from app.api.v1.models.add_services import AddServicesModel
from app.api.v1.models.auth import UsersModel
from utils.utils import check_add_services_keys, raise_error, convert_to_int, is_valid_phone
from flask_jwt_extended import jwt_required

add_services_v1 = Blueprint('add_services_v1', __name__)


@add_services_v1.route('/add_services', methods=['POST'])
def add_service():
    """A registered user can add a service that he or she offers."""
    errors = check_add_services_keys(request)
    if errors:
        return raise_error(400, "Invalid {} key".format(', '.join(errors)))
    details = request.get_json()
    portfolio = details['portfolio']
    occupation = details['occupation']
    phone = details['phone']
    location = details['location']
    img = details['img']
    cost = details['cost']
    if not is_valid_phone(phone):
        return raise_error(400, "Invalid phone number!")
    service = AddServicesModel(
        portfolio, occupation, phone, location, img, cost).save()
    return make_response(jsonify({
        "status": "201",
        "message": "You have successfully added the service!",
        "service": service
    }), 201)


@add_services_v1.route('/add_services', methods=['GET'])
def get_all_services():
    '''Fetch all the existing services.'''
    return make_response(jsonify({
        "status": "200",
        "message": "success",
        "hotels": json.loads(AddServicesModel().get_services())
    }), 200)


@add_services_v1.route('/add_services/<string:occupation>', methods=['GET'])
def get_specific_service(occupation):
    """Fetch a specific service."""
    service = AddServicesModel().get_service(occupation)
    service = json.loads(service)
    if service:
        return make_response(jsonify({
            "status": "200",
            "message": "success",
            "service": service
        }), 200)
    return make_response(jsonify({
        "status": "404",
        "message": "service not found"
    }), 404)
