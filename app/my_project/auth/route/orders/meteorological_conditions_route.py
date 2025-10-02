from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import meteorological_conditions_controller
from lab4.app.my_project.auth.domain import MeteorologicalConditions

meteorological_conditions_bp = Blueprint('meteorological_conditions', __name__, url_prefix='/meteorological-conditions')


@meteorological_conditions_bp.get('')
def get_all_meteorological_conditions() -> Response:
    """
    Get all meteorological conditions
    ---
    responses:
      200:
        description: List of all meteorological conditions
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(meteorological_conditions_controller.find_all()), HTTPStatus.OK)


@meteorological_conditions_bp.post('')
def create_meteorological_conditions() -> Response:
    """
    Create a new meteorological condition
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              condition_name:
                type: string
                description: Name of the meteorological condition
              value:
                type: number
                description: Value of the condition
              unit:
                type: string
                description: Unit of measurement
    responses:
      201:
        description: Meteorological condition created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    meteorological_conditions = MeteorologicalConditions.create_from_dto(content)
    meteorological_conditions_controller.create(meteorological_conditions)
    return make_response(jsonify(meteorological_conditions.put_into_dto()), HTTPStatus.CREATED)


@meteorological_conditions_bp.get('/<int:meteorological_conditions_id>')
def get_meteorological_conditions(meteorological_conditions_id: int) -> Response:
    """
    Get meteorological condition by ID
    ---
    parameters:
      - name: meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the meteorological condition
    responses:
      200:
        description: Meteorological condition found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(meteorological_conditions_controller.find_by_id(meteorological_conditions_id)),
                         HTTPStatus.OK)


@meteorological_conditions_bp.put('/<int:meteorological_conditions_id>')
def update_meteorological_conditions(meteorological_conditions_id: int) -> Response:
    """
    Update meteorological condition by ID
    ---
    parameters:
      - name: meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the meteorological condition
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              condition_name:
                type: string
              value:
                type: number
              unit:
                type: string
    responses:
      200:
        description: Meteorological condition updated successfully
    """
    content = request.get_json()
    meteorological_conditions = MeteorologicalConditions.create_from_dto(content)
    meteorological_conditions_controller.update(meteorological_conditions_id, meteorological_conditions)
    return make_response("MeteorologicalConditions updated", HTTPStatus.OK)


@meteorological_conditions_bp.patch('/<int:meteorological_conditions_id>')
def patch_meteorological_conditions(meteorological_conditions_id: int) -> Response:
    """
    Partially update meteorological condition by ID
    ---
    parameters:
      - name: meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the meteorological condition
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the meteorological condition
    responses:
      200:
        description: Meteorological condition patched successfully
    """
    content = request.get_json()
    meteorological_conditions_controller.patch(meteorological_conditions_id, content)
    return make_response("MeteorologicalConditions updated", HTTPStatus.OK)


@meteorological_conditions_bp.delete('/<int:meteorological_conditions_id>')
def delete_meteorological_conditions(meteorological_conditions_id: int) -> Response:
    """
    Delete meteorological condition by ID
    ---
    parameters:
      - name: meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the meteorological condition
    responses:
      200:
        description: Meteorological condition deleted successfully
    """
    meteorological_conditions_controller.delete(meteorological_conditions_id)
    return make_response("MeteorologicalConditions deleted", HTTPStatus.OK)
