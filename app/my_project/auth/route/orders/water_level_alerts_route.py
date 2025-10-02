from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import water_level_alerts_controller
from lab4.app.my_project.auth.domain import WaterLevelAlerts

water_level_alerts_bp = Blueprint('water-level-alerts', __name__, url_prefix='/water-level-alerts')


@water_level_alerts_bp.get('')
def get_all_water_level_alerts() -> Response:
    """
    Get all water level alerts
    ---
    responses:
      200:
        description: List of all water level alerts
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(water_level_alerts_controller.find_all()), HTTPStatus.OK)


@water_level_alerts_bp.post('')
def create_water_level_alerts() -> Response:
    """
    Create a new water level alert
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              alert_name:
                type: string
                description: Name of the alert
              threshold:
                type: number
                description: Threshold value for the alert
              measurement_locations_id:
                type: integer
                description: Measurement location ID
    responses:
      201:
        description: Water level alert created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    water_level_alerts = WaterLevelAlerts.create_from_dto(content)
    water_level_alerts_controller.create(water_level_alerts)
    return make_response(jsonify(water_level_alerts.put_into_dto()), HTTPStatus.CREATED)


@water_level_alerts_bp.get('/<int:water_level_alerts_id>')
def get_water_level_alerts(water_level_alerts_id: int) -> Response:
    """
    Get water level alert by ID
    ---
    parameters:
      - name: water_level_alerts_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level alert
    responses:
      200:
        description: Water level alert found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(water_level_alerts_controller.find_by_id(water_level_alerts_id)), HTTPStatus.OK)


@water_level_alerts_bp.put('/<int:water_level_alerts_id>')
def update_water_level_alerts(water_level_alerts_id: int) -> Response:
    """
    Update water level alert by ID
    ---
    parameters:
      - name: water_level_alerts_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level alert
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              alert_name:
                type: string
              threshold:
                type: number
              measurement_locations_id:
                type: integer
    responses:
      200:
        description: Water level alert updated successfully
    """
    content = request.get_json()
    water_level_alerts = WaterLevelAlerts.create_from_dto(content)
    water_level_alerts_controller.update(water_level_alerts_id, water_level_alerts)
    return make_response("WaterLevelAlerts updated", HTTPStatus.OK)


@water_level_alerts_bp.patch('/<int:water_level_alerts_id>')
def patch_water_level_alerts(water_level_alerts_id: int) -> Response:
    """
    Partially update water level alert by ID
    ---
    parameters:
      - name: water_level_alerts_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level alert
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the water level alert
    responses:
      200:
        description: Water level alert patched successfully
    """
    content = request.get_json()
    water_level_alerts_controller.patch(water_level_alerts_id, content)
    return make_response("WaterLevelAlerts updated", HTTPStatus.OK)


@water_level_alerts_bp.delete('/<int:water_level_alerts_id>')
def delete_water_level_alerts(water_level_alerts_id: int) -> Response:
    """
    Delete water level alert by ID
    ---
    parameters:
      - name: water_level_alerts_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the water level alert
    responses:
      200:
        description: Water level alert deleted successfully
    """
    water_level_alerts_controller.delete(water_level_alerts_id)
    return make_response("WaterLevelAlerts deleted", HTTPStatus.OK)


@water_level_alerts_bp.get('/get-water-level-alerts-by-measurement-location/<int:measurement_locations_id>')
def get_water_level_alerts_after_measurement_locations(measurement_locations_id: int) -> Response:
    """
    Get water level alerts by measurement location ID
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
        description: List of water level alerts for the measurement location
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(water_level_alerts_controller.
                                 get_water_level_alerts_after_measurement_locations(measurement_locations_id)),
                         HTTPStatus.OK)
