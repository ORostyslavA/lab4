from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import water_levels_controller
from lab4.app.my_project.auth.domain import WaterLevels

water_levels_bp = Blueprint('water_levels', __name__, url_prefix='/water-levels')


@water_levels_bp.get('')
def get_all_water_levels() -> Response:
    """
    Get all water levels
    ---
    responses:
      200:
        description: List of all water levels
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(water_levels_controller.find_all()), HTTPStatus.OK)


@water_levels_bp.post('')
def create_water_levels() -> Response:
    """
    Create a new water level
    ---
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          required:
            - measurement_location_id
            - level
            - measured_at
          properties:
            measurement_location_id:
              type: integer
              description: Measurement location ID
            level:
              type: number
              format: float
              description: Water level value
            measured_at:
              type: string
              format: date-time
              description: Time when level was measured
            note:
              type: string
              description: Optional note
    responses:
      201:
        description: Water level created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    water_levels = WaterLevels.create_from_dto(content)
    water_levels_controller.create(water_levels)
    return make_response(jsonify(water_levels.put_into_dto()), HTTPStatus.CREATED)


@water_levels_bp.get('/<int:water_levels_id>')
def get_water_levels(water_levels_id: int) -> Response:
    """
    Get water level by ID
    ---
    parameters:
      - name: water_levels_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level
    responses:
      200:
        description: Water level found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(water_levels_controller.find_by_id(water_levels_id)), HTTPStatus.OK)


@water_levels_bp.put('/<int:water_levels_id>')
def update_water_levels(water_levels_id: int) -> Response:
    """
    Update water level by ID
    ---
    parameters:
      - name: water_levels_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          properties:
            measurement_location_id:
              type: integer
            level:
              type: number
              format: float
            measured_at:
              type: string
              format: date-time
            note:
              type: string
    responses:
      200:
        description: Water level updated successfully
    """
    content = request.get_json()
    water_levels = WaterLevels.create_from_dto(content)
    water_levels_controller.update(water_levels_id, water_levels)
    return make_response("WaterLevels updated", HTTPStatus.OK)


@water_levels_bp.patch('/<int:water_levels_id>')
def patch_water_levels(water_levels_id: int) -> Response:
    """
    Partially update water level by ID
    ---
    parameters:
      - name: water_levels_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level
    consumes:
      - application/json
    parameters:
      - in: body
        name: body
        required: true
        schema:
          type: object
          description: Fields to update in the water level
    responses:
      200:
        description: Water level patched successfully
    """
    content = request.get_json()
    water_levels_controller.patch(water_levels_id, content)
    return make_response("WaterLevels updated", HTTPStatus.OK)


@water_levels_bp.delete('/<int:water_levels_id>')
def delete_water_levels(water_levels_id: int) -> Response:
    """
    Delete water level by ID
    ---
    parameters:
      - name: water_levels_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level
    responses:
      200:
        description: Water level deleted successfully
    """
    water_levels_controller.delete(water_levels_id)
    return make_response("WaterLevels deleted", HTTPStatus.OK)


@water_levels_bp.get('/get-water-levels-measurement-location/<int:measurement_locations_id>')
def get_water_levels_after_measurement_locations(measurement_locations_id: int) -> Response:
    """
    Get water levels by measurement location ID
    ---
    parameters:
      - name: measurement_locations_id
        in: path
        required: true
        schema:
          type: integer
        description: Measurement location ID
    responses:
      200:
        description: List of water levels for the measurement location
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(water_levels_controller.
                                 get_water_levels_after_measurement_locations(measurement_locations_id)), HTTPStatus.OK)
