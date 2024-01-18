from os import environ
import importlib

from flask import jsonify, request
from models.users import *
from services.users import *

module = importlib.import_module(environ.get("STAGE_ENV"))

app = module.app

route_prefix = '/users'

# For testing purposes
@app.route(route_prefix + "/")
def test():
    return "Hello World"

@app.route(route_prefix + "/get_all_users")
def get_all_users():
    user_list = get_all_user()
    if user_list:
        return jsonify(
            {
                "code": 200,
                "data": user_list
            }
        )
    return jsonify(
        {
            "code": 400,
            "message": "No users found."
        }
    )

@app.route(route_prefix + "/get_user_by_user_id/<string:user_id>")
def get_specific_user(user_id):
    user = get_user_by_user_id(user_id)
    print(user)
    if user:
        return jsonify(
            {
                "code": 200,
                "data": user
            }
        )
    return jsonify(
        {
            "code": 400,
            "message": "User with {} not found.".format(user_id)
        }
    )

@app.route(route_prefix + "/register_user", methods=['POST'])
def register_user():

    data = request.get_json()

    print(data)

    if get_user_by_email(data['email']):
        return jsonify(
            {
                "code": 400,
                "message": "{} has already been use for registration.".format(data['email'])
            }
        )

    user_registration_status = register_user_service(data['first_name'], data['last_name'], data['password'], data['email'])
    
    print(user_registration_status)

    if user_registration_status:
        return jsonify(
            {
                "code": 200,
                "message": "User registered succesfully."
            }
        )
    
    return jsonify(
        {
            "code": 400,
            "message": "User registration failed."
        }
    )


@app.route(route_prefix + "/login", methods=['POST'])
def login():

    data = request.get_json()
    code = 200
    message = ""

    print(data)

    authentication_status = authenticate_user(data['email'], data['password'])

    print(authentication_status)

    match authentication_status:
        case 0:
            code = 400
            message = "User not found."
        case 1:
            code = 400
            message = "Wrong password."
        case 2:
            message = "User aunthenticated succesfully."

    return jsonify(
        {
            "code": code,
            "message": message
        }
    )