from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import users_has_water_level_alerts_controller
from lab4.app.my_project.auth.domain import UsersHasWaterLevelAlerts

users_has_water_level_alerts_bp = Blueprint('users_has_water_level_alerts', __name__,
                                            url_prefix='/users-has-water-level-alerts')


@users_has_water_level_alerts_bp.get('')
def get_all_users_has_water_level_alerts() -> Response:
    """
    Get all user-water-level-alerts relations
    ---
    responses:
      200:
        description: List of all user-water-level-alerts relations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(users_has_water_level_alerts_controller.find_all()), HTTPStatus.OK)


@users_has_water_level_alerts_bp.post('')
def create_users_has_water_level_alerts() -> Response:
    """
    Create a new user-water-level-alerts relation
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              users_id:
                type: integer
                description: User ID
              water_level_alerts_id:
                type: integer
                description: Water level alert ID
    responses:
      201:
        description: Relation created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    users_has_water_level_alerts = UsersHasWaterLevelAlerts.create_from_dto(content)
    users_has_water_level_alerts_controller.create(users_has_water_level_alerts)
    return make_response(jsonify(users_has_water_level_alerts.put_into_dto()), HTTPStatus.CREATED)


@users_has_water_level_alerts_bp.get('/<int:users_has_water_level_alerts_id>')
def get_users_has_water_level_alerts(users_has_water_level_alerts_id: int) -> Response:
    """
    Get user-water-level-alerts relation by ID
    ---
    parameters:
      - name: users_has_water_level_alerts_id
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
    return make_response(jsonify(users_has_water_level_alerts_controller.find_by_id(users_has_water_level_alerts_id)),
                         HTTPStatus.OK)


@users_has_water_level_alerts_bp.put('/<int:users_has_water_level_alerts_id>')
def update_users_has_water_level_alerts(users_has_water_level_alerts_id: int) -> Response:
    """
    Update user-water-level-alerts relation by ID
    ---
    parameters:
      - name: users_has_water_level_alerts_id
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
              users_id:
                type: integer
              water_level_alerts_id:
                type: integer
    responses:
      200:
        description: Relation updated successfully
    """
    content = request.get_json()
    users_has_water_level_alerts = UsersHasWaterLevelAlerts.create_from_dto(content)
    users_has_water_level_alerts_controller.update(users_has_water_level_alerts_id, users_has_water_level_alerts)
    return make_response("UsersHasWaterLevelAlerts updated", HTTPStatus.OK)


@users_has_water_level_alerts_bp.patch('/<int:users_has_water_level_alerts_id>')
def patch_water_level_alerts(users_has_water_level_alerts_id: int) -> Response:
    """
    Partially update user-water-level-alerts relation by ID
    ---
    parameters:
      - name: users_has_water_level_alerts_id
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
    users_has_water_level_alerts_controller.patch(users_has_water_level_alerts_id, content)
    return make_response("UsersHasWaterLevelAlerts updated", HTTPStatus.OK)


@users_has_water_level_alerts_bp.delete('/<int:users_has_water_level_alerts_id>')
def delete_users_has_water_level_alerts(users_has_water_level_alerts_id: int) -> Response:
    """
    Delete user-water-level-alerts relation by ID
    ---
    parameters:
      - name: users_has_water_level_alerts_id
        in: path
        required: true
        schema:
          type: integer
        description: Relation ID
    responses:
      200:
        description: Relation deleted successfully
    """
    users_has_water_level_alerts_controller.delete(users_has_water_level_alerts_id)
    return make_response("UsersHasWaterLevelAlerts deleted", HTTPStatus.OK)


@users_has_water_level_alerts_bp.get('/get-users/<int:users_id>')
def get_users(users_id: int) -> Response:
    """
    Get all water level alerts for a user
    ---
    parameters:
      - name: users_id
        in: path
        required: true
        schema:
          type: integer
        description: User ID
    responses:
      200:
        description: List of water level alerts for the user
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(users_has_water_level_alerts_controller.get_users(users_id)), HTTPStatus.OK)


@users_has_water_level_alerts_bp.get('/get-water-level-alerts/<int:water_level_alerts_id>')
def get_water_level_alerts(water_level_alerts_id: int) -> Response:
    """
    Get all users for a water level alert
    ---
    parameters:
      - name: water_level_alerts_id
        in: path
        required: true
        schema:
          type: integer
        description: Water level alert ID
    responses:
      200:
        description: List of users for the water level alert
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(users_has_water_level_alerts_controller.get_water_level_alerts(water_level_alerts_id)),
                         HTTPStatus.OK)
