import re

from flask import jsonify, make_response


def check_register_keys(request):
    res_keys = ['firstname', 'lastname', 'surname', 'admission_no', 'email', 'password', 'form']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors

def check_exams_keys(request):
    res_keys = ['admission_no', 'maths', 'english', 'kiswahili', 'chemistry', 'biology', 'physics', 'history', 'geography', 'cre', 'agriculture', 'business']
    errors = []
    for key in res_keys:
        if not key in request.json:
            errors.append(key)
    return errors


def raise_error(status, msg):
    return make_response(jsonify({
        "status": "400",
        "message": msg
    }), status)


def is_valid_email(variable):
    """Check if email is a valid mail."""
    if re.match(r"(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+[a-zA-Z0-9-.]+$)",
                variable):
        return True
    return False


def is_valid_password(variable):
    """Check if password is a valid password."""
    if re.match(r'[A-Za-z0-9@#$%^&+=]{8,}', variable):
        return True
    return False


def form_restrictions(data):
    """Restrict user inputs in a list."""

    form = ["1", "2", "3", "4"]
    if data not in form:
        return False
    return True

def subjects(data):
    """Restrict user inputs in a list."""

    subject = ["R", "r", "NR", "nr"]
    if data not in subject:
        return False
    return True
