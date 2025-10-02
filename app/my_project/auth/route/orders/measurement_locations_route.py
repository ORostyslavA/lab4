from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import measurement_locations_controller
from lab4.app.my_project.auth.domain import MeasurementLocations

measurement_locations_bp = Blueprint('measurement-locations', __name__, url_prefix='/measurement-locations')


@measurement_locations_bp.get('')
def get_all_measurement_locations() -> Response:
    """
    Get all measurement locations
    ---
    responses:
      200:
        description: List of all measurement locations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(measurement_locations_controller.find_all()), HTTPStatus.OK)


@measurement_locations_bp.post('')
def create_measurement_locations() -> Response:
    """
    Create a new measurement location
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              location_name:
                type: string
                description: Name of the measurement location
              latitude:
                type: number
                description: Latitude coordinate
              longitude:
                type: number
                description: Longitude coordinate
              rivers_id:
                type: integer
                description: River ID
              regions_id:
                type: integer
                description: Region ID
    responses:
      201:
        description: Measurement location created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    measurement_locations = MeasurementLocations.create_from_dto(content)
    measurement_locations_controller.create(measurement_locations)
    return make_response(jsonify(measurement_locations.put_into_dto()), HTTPStatus.CREATED)


@measurement_locations_bp.get('/<int:measurement_locations_id>')
def get_measurement_locations(measurement_locations_id: int) -> Response:
    """
    Get measurement location by ID
    ---
    parameters:
      - name: measurement_locations_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the measurement location
    responses:
      200:
        description: Measurement location found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(measurement_locations_controller.find_by_id(measurement_locations_id)), HTTPStatus.OK)


@measurement_locations_bp.put('/<int:measurement_locations_id>')
def update_measurement_locations(measurement_locations_id: int) -> Response:
    """
    Update measurement location by ID
    ---
    parameters:
      - name: measurement_locations_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the measurement location
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              location_name:
                type: string
              latitude:
                type: number
              longitude:
                type: number
              rivers_id:
                type: integer
              regions_id:
                type: integer
    responses:
      200:
        description: Measurement location updated successfully
    """
    content = request.get_json()
    measurement_locations = MeasurementLocations.create_from_dto(content)
    measurement_locations_controller.update(measurement_locations_id, measurement_locations)
    return make_response("MeasurementLocations updated", HTTPStatus.OK)


@measurement_locations_bp.patch('/<int:measurement_locations_id>')
def patch_measurement_locations(measurement_locations_id: int) -> Response:
    """
    Partially update measurement location by ID
    ---
    parameters:
      - name: measurement_locations_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the measurement location
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the measurement location
    responses:
      200:
        description: Measurement location patched successfully
    """
    content = request.get_json()
    measurement_locations_controller.patch(measurement_locations_id, content)
    return make_response("MeasurementLocations updated", HTTPStatus.OK)


@measurement_locations_bp.delete('/<int:measurement_locations_id>')
def delete_measurement_locations(measurement_locations_id: int) -> Response:
    """
    Delete measurement location by ID
    ---
    parameters:
      - name: measurement_locations_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the measurement location
    responses:
      200:
        description: Measurement location deleted successfully
    """
    measurement_locations_controller.delete(measurement_locations_id)
    return make_response("MeasurementLocations deleted", HTTPStatus.OK)


@measurement_locations_bp.get('/get-measurement-locations-by-river/<int:rivers_id>')
def get_measurement_locations_after_rivers(rivers_id: int) -> Response:
    """
    Get measurement locations by river ID
    ---
    parameters:
      - name: rivers_id
        in: path
        required: true
        schema:
          type: integer
        description: River ID
    responses:
      200:
        description: List of measurement locations for the river
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(measurement_locations_controller.get_measurement_locations_after_rivers(rivers_id)),
                         HTTPStatus.OK)


@measurement_locations_bp.get('/get-measurement-locations-by-region/<int:regions_id>')
def get_measurement_locations_after_regions(regions_id: int) -> Response:
    """
    Get measurement locations by region ID
    ---
    parameters:
      - name: regions_id
        in: path
        required: true
        schema:
          type: integer
        description: Region ID
    responses:
      200:
        description: List of measurement locations for the region
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(measurement_locations_controller.get_measurement_locations_after_regions(regions_id)),
                         HTTPStatus.OK)
