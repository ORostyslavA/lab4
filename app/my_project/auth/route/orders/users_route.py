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
        description: List of all users
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
    Create a new user
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
                description: Username of the user
              email:
                type: string
                description: Email address of the user
              password:
                type: string
                description: Password for the user
    responses:
      201:
        description: User created successfully
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
    Get user by ID
    ---
    parameters:
      - name: users_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the user
    responses:
      200:
        description: User found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(users_controller.find_by_id(users_id)), HTTPStatus.OK)


@users_bp.put('/<int:users_id>')
def update_users(users_id: int) -> Response:
    """
    Update user by ID
    ---
    parameters:
      - name: users_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the user
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              username:
                type: string
              email:
                type: string
              password:
                type: string
    responses:
      200:
        description: User updated successfully
    """
    content = request.get_json()
    users = Users.create_from_dto(content)
    users_controller.update(users_id, users)
    return make_response("Users updated", HTTPStatus.OK)


@users_bp.patch('/<int:users_id>')
def patch_users(users_id: int) -> Response:
    """
    Partially update user by ID
    ---
    parameters:
      - name: users_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the user
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the user
    responses:
      200:
        description: User patched successfully
    """
    content = request.get_json()
    users_controller.patch(users_id, content)
    return make_response("Users updated", HTTPStatus.OK)


@users_bp.delete('/<int:users_id>')
def delete_users(users_id: int) -> Response:
    """
    Delete user by ID
    ---
    parameters:
      - name: users_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the user
    responses:
      200:
        description: User deleted successfully
    """
    users_controller.delete(users_id)
    return make_response("Users deleted", HTTPStatus.OK)
