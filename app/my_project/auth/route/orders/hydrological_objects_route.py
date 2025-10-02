from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import hydrological_objects_controller
from lab4.app.my_project.auth.domain import HydrologicalObjects

hydrological_objects_bp = Blueprint('hydrological_objects', __name__, url_prefix='/hydrological-objects')


@hydrological_objects_bp.get('')
def get_all_hydrological_objects() -> Response:
    """
    Get all hydrological objects
    ---
    responses:
      200:
        description: List of all hydrological objects
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hydrological_objects_controller.find_all()), HTTPStatus.OK)


@hydrological_objects_bp.post('')
def create_hydrological_objects() -> Response:
    """
    Create a new hydrological object
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              object_name:
                type: string
                description: Name of the hydrological object
              object_type:
                type: string
                description: Type of the hydrological object
              region_id:
                type: integer
                description: Region ID
    responses:
      201:
        description: Hydrological object created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    hydrological_objects = HydrologicalObjects.create_from_dto(content)
    hydrological_objects_controller.create(hydrological_objects)
    return make_response(jsonify(hydrological_objects.put_into_dto()), HTTPStatus.CREATED)


@hydrological_objects_bp.get('/<int:hydrological_objects_id>')
def get_hydrological_objects(hydrological_objects_id: int) -> Response:
    """
    Get hydrological object by ID
    ---
    parameters:
      - name: hydrological_objects_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the hydrological object
    responses:
      200:
        description: Hydrological object found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(hydrological_objects_controller.find_by_id(hydrological_objects_id)), HTTPStatus.OK)


@hydrological_objects_bp.put('/<int:hydrological_objects_id>')
def update_hydrological_objects(hydrological_objects_id: int) -> Response:
    """
    Update hydrological object by ID
    ---
    parameters:
      - name: hydrological_objects_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the hydrological object
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              object_name:
                type: string
              object_type:
                type: string
              region_id:
                type: integer
    responses:
      200:
        description: Hydrological object updated successfully
    """
    content = request.get_json()
    hydrological_objects = HydrologicalObjects.create_from_dto(content)
    hydrological_objects_controller.update(hydrological_objects_id, hydrological_objects)
    return make_response("HydrologicalObjects updated", HTTPStatus.OK)


@hydrological_objects_bp.patch('/<int:hydrological_objects_id>')
def patch_hydrological_objects(hydrological_objects_id: int) -> Response:
    """
    Partially update hydrological object by ID
    ---
    parameters:
      - name: hydrological_objects_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the hydrological object
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the hydrological object
    responses:
      200:
        description: Hydrological object patched successfully
    """
    content = request.get_json()
    hydrological_objects_controller.patch(hydrological_objects_id, content)
    return make_response("HydrologicalObjects updated", HTTPStatus.OK)


@hydrological_objects_bp.delete('/<int:hydrological_objects_id>')
def delete_hydrological_objects(hydrological_objects_id: int) -> Response:
    """
    Delete hydrological object by ID
    ---
    parameters:
      - name: hydrological_objects_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the hydrological object
    responses:
      200:
        description: Hydrological object deleted successfully
    """
    hydrological_objects_controller.delete(hydrological_objects_id)
    return make_response("HydrologicalObjects deleted", HTTPStatus.OK)
