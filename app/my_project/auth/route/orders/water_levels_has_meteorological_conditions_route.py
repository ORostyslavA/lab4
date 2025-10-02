from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import water_levels_has_meteorological_conditions_controller
from lab4.app.my_project.auth.domain import WaterLevelsHasMeteorologicalConditions

water_levels_has_meteorological_conditions_bp = Blueprint('water_levels_has_meteorological_conditions', __name__,
                                                          url_prefix='/water-levels-has-meteorological-conditions')


@water_levels_has_meteorological_conditions_bp.get('')
def get_all_water_levels_has_meteorological_conditions() -> Response:
    """
    Get all water-levels-has-meteorological-conditions relations
    ---
    responses:
      200:
        description: List of all water-levels-has-meteorological-conditions relations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(water_levels_has_meteorological_conditions_controller.find_all()), HTTPStatus.OK)


@water_levels_has_meteorological_conditions_bp.post('')
def create_water_levels_has_meteorological_conditions() -> Response:
    """
    Create a new water-levels-has-meteorological-conditions relation
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              water_levels_id:
                type: integer
                description: Water level ID
              meteorological_conditions_id:
                type: integer
                description: Meteorological condition ID
    responses:
      201:
        description: Relation created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    water_levels_has_meteorological_conditions = WaterLevelsHasMeteorologicalConditions.create_from_dto(content)
    water_levels_has_meteorological_conditions_controller.create(water_levels_has_meteorological_conditions)
    return make_response(jsonify(water_levels_has_meteorological_conditions.put_into_dto()), HTTPStatus.CREATED)


@water_levels_has_meteorological_conditions_bp.get('/<int:water_levels_has_meteorological_conditions_id>')
def get_water_levels_has_meteorological_conditions(water_levels_has_meteorological_conditions_id: int) -> Response:
    """
    Get water-levels-has-meteorological-conditions relation by ID
    ---
    parameters:
      - name: water_levels_has_meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: Relation ID
    responses:
      200:
        description: Relation found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(water_levels_has_meteorological_conditions_controller.
                                 find_by_id(water_levels_has_meteorological_conditions_id)), HTTPStatus.OK)


@water_levels_has_meteorological_conditions_bp.put('/<int:water_levels_has_meteorological_conditions_id>')
def update_water_levels_has_meteorological_conditions(water_levels_has_meteorological_conditions_id: int) -> Response:
    """
    Update water-levels-has-meteorological-conditions relation by ID
    ---
    parameters:
      - name: water_levels_has_meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: Relation ID
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              water_levels_id:
                type: integer
              meteorological_conditions_id:
                type: integer
    responses:
      200:
        description: Relation updated successfully
    """
    content = request.get_json()
    water_levels_has_meteorological_conditions = WaterLevelsHasMeteorologicalConditions.create_from_dto(content)
    water_levels_has_meteorological_conditions_controller.update(water_levels_has_meteorological_conditions_id,
                                                                 water_levels_has_meteorological_conditions)
    return make_response("WaterLevelsHasMeteorologicalConditions updated", HTTPStatus.OK)


@water_levels_has_meteorological_conditions_bp.patch('/<int:water_levels_has_meteorological_conditions_id>')
def patch_water_levels_has_meteorological_conditions(water_levels_has_meteorological_conditions_id: int) -> Response:
    """
    Partially update water-levels-has-meteorological-conditions relation by ID
    ---
    parameters:
      - name: water_levels_has_meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: Relation ID
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the relation
    responses:
      200:
        description: Relation patched successfully
    """
    content = request.get_json()
    water_levels_has_meteorological_conditions_controller.patch(water_levels_has_meteorological_conditions_id, content)
    return make_response("WaterLevelsHasMeteorologicalConditions updated", HTTPStatus.OK)


@water_levels_has_meteorological_conditions_bp.delete('/<int:water_levels_has_meteorological_conditions_id>')
def delete_water_levels_has_meteorological_conditions(water_levels_has_meteorological_conditions_id: int) -> Response:
    """
    Delete water-levels-has-meteorological-conditions relation by ID
    ---
    parameters:
      - name: water_levels_has_meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: Relation ID
    responses:
      200:
        description: Relation deleted successfully
    """
    water_levels_has_meteorological_conditions_controller.delete(water_levels_has_meteorological_conditions_id)
    return make_response("WaterLevelsHasMeteorologicalConditions deleted", HTTPStatus.OK)


@water_levels_has_meteorological_conditions_bp.get('/get-water-levels/<int:water_levels_id>')
def get_water_levels(water_levels_id: int) -> Response:
    """
    Get meteorological conditions for a water level
    ---
    parameters:
      - name: water_levels_id
        in: path
        required: true
        schema:
          type: integer
        description: Water level ID
    responses:
      200:
        description: List of meteorological conditions for the water level
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(
        jsonify(water_levels_has_meteorological_conditions_controller.get_water_levels(water_levels_id)),
        HTTPStatus.OK)


@water_levels_has_meteorological_conditions_bp.get('/get-meteorological-conditions/<int:meteorological_conditions_id>')
def get_meteorological_conditions(meteorological_conditions_id: int) -> Response:
    """
    Get water levels for a meteorological condition
    ---
    parameters:
      - name: meteorological_conditions_id
        in: path
        required: true
        schema:
          type: integer
        description: Meteorological condition ID
    responses:
      200:
        description: List of water levels for the meteorological condition
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(water_levels_has_meteorological_conditions_controller.
                                 get_meteorological_conditions(meteorological_conditions_id)),
                         HTTPStatus.OK)
