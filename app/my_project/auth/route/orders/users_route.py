from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import users_controller
from lab4.app.my_project.auth.domain import Users

users_bp = Blueprint('users', __name__, url_prefix='/users')


@users_bp.get('')
def get_all_users() -> Response:
    """
    Get all users
    ---
    responses:
      200:
        description: Returns a list of users
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(users_controller.find_all()), HTTPStatus.OK)


@users_bp.post('')
def create_users() -> Response:
    """
    Create a new city
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_name:
              type: string
              description: The name of the city
            user_surname:
              type: string
              description: The surname of the user
            user_email:
              type: string
              description: The email of the user
          required:
            - user_name
            - user_surname
            - user_email
    responses:
      201:
        description: Returns the created city
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    users = Users.create_from_dto(content)
    users_controller.create(users)
    return make_response(jsonify(users.put_into_dto()), HTTPStatus.CREATED)


@users_bp.get('/<int:users_id>')
def get_users(users_id: int) -> Response:
    """
    Get a city by ID
    ---
    parameters:
      - in: path
        name: users_id
        required: true
        schema:
          type: integer
        description: The ID of the user
    responses:
      200:
        description: Returns the user
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(users_controller.find_by_id(users_id)), HTTPStatus.OK)


@users_bp.put('/<int:users_id>')
def update_users(users_id: int) -> Response:
    """
    Update a user by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: users_id
        required: true
        schema:
          type: integer
        description: The ID of the city
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            user_name:
              type: string
              description: The name of the city
            user_surname:
              type: string
              description: The surname of the user
            user_email:
              type: string
              description: The email of the user
          required:
            - user_name
            - user_surname
            - user_email
    responses:
      200:
        description: City updated
    """
    content = request.get_json()
    users = Users.create_from_dto(content)
    users_controller.update(users_id, users)
    return make_response("Users updated", HTTPStatus.OK)


@users_bp.patch('/<int:users_id>')
def patch_users(users_id: int) -> Response:
    """
    Patch a city by ID
    ---
    consumes:
      - application/json
    parameters:
      - in: path
        name: users_id
        required: true
        schema:
          type: integer
        description: The ID of the user
      - in: body
        name: body
        required: true
        schema:
          type: object
    responses:
      200:
        description: City updated
    """
    content = request.get_json()
    users_controller.patch(users_id, content)
    return make_response("Users updated", HTTPStatus.OK)


@users_bp.delete('/<int:users_id>')
def delete_users(users_id: int) -> Response:
    """
    Delete a city by ID
    ---
    parameters:
      - in: path
        name: users_id
        required: true
        schema:
          type: integer
        description: The ID of the city
    responses:
      200:
        description: City deleted
    """
    users_controller.delete(users_id)
    return make_response("Users deleted", HTTPStatus.OK)
