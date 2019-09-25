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
    name = details['name']
    business_name = details['business_name']
    portfolio = details['portfolio']
    occupation = details['occupation']
    description = details['description']
    phone = details['phone']
    location = details['location']
    working_hours = details['working_hours']
    cost = details['cost']
    service = AddServicesModel(
        name, business_name, portfolio, occupation, description, phone, location, working_hours, cost).save()
    return make_response(jsonify({
        "status": "201",
        "message": "You have successfully added the service!",
        "service": service
    }), 201)


@add_services_v1.route('/add_services', methods=['GET'])
def get_all_services():
    '''Fetch all the existing services.'''
    services = AddServicesModel().get_services()
    return make_response(jsonify({
        "status": "200",
        "message": "success",
        "services": services
    }), 200)


@add_services_v1.route('/add_services/<occupation>', methods=['GET'])
def get_specific_service(occupation):
    """Fetch a specific service."""
    service = AddServicesModel().get_service(occupation)
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
