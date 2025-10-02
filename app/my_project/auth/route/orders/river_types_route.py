from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import river_types_controller
from lab4.app.my_project.auth.domain import RiverTypes

river_types_bp = Blueprint('river-types', __name__, url_prefix='/river-types')


@river_types_bp.get('')
def get_all_river_types() -> Response:
    """
    Example endpoint returning river types
    ---
    responses:
      200:
        description: A successful response
    """
    return make_response(jsonify(river_types_controller.find_all()), HTTPStatus.OK)


@river_types_bp.post('')
def create_river_types() -> Response:
    """
    Create a new river type
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              type_description:
                type: string
                description: Description of the river type
    responses:
      201:
        description: River type created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    river_types = RiverTypes.create_from_dto(content)
    river_types_controller.create(river_types)
    return make_response(jsonify(river_types.put_into_dto()), HTTPStatus.CREATED)


@river_types_bp.get('/<int:river_types_id>')
def get_river_types(river_types_id: int) -> Response:
    """
    Get river type by ID
    ---
    parameters:
      - name: river_types_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river type
    responses:
      200:
        description: River type found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(river_types_controller.find_by_id(river_types_id)), HTTPStatus.OK)


@river_types_bp.put('/<int:river_types_id>')
def update_river_types(river_types_id: int) -> Response:
    """
    Update river type by ID
    ---
    parameters:
      - name: river_types_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river type
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              type_description:
                type: string
                description: Updated description of the river type
    responses:
      200:
        description: River type updated successfully
    """
    content = request.get_json()
    river_types = RiverTypes.create_from_dto(content)
    river_types_controller.update(river_types_id, river_types)
    return make_response("RiverTypes updated", HTTPStatus.OK)


@river_types_bp.patch('/<int:river_types_id>')
def patch_river_types(river_types_id: int) -> Response:
    """
    Partially update river type by ID
    ---
    parameters:
      - name: river_types_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river type
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the river type
    responses:
      200:
        description: River type patched successfully
    """
    content = request.get_json()
    river_types_controller.patch(river_types_id, content)
    return make_response("RiverTypes updated", HTTPStatus.OK)


@river_types_bp.delete('/<int:river_types_id>')
def delete_river_types(river_types_id: int) -> Response:
    """
    Delete river type by ID
    ---
    parameters:
      - name: river_types_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river type
    responses:
      200:
        description: River type deleted successfully
    """
    river_types_controller.delete(river_types_id)
    return make_response("RiverTypes deleted", HTTPStatus.OK)




