from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import rivers_controller
from lab4.app.my_project.auth.domain import Rivers

rivers_bp = Blueprint('rivers', __name__, url_prefix='/rivers')


@rivers_bp.get('')
def get_all_rivers() -> Response:
    """
    Get all rivers
    ---
    responses:
      200:
        description: List of all rivers
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(rivers_controller.find_all()), HTTPStatus.OK)


@rivers_bp.post('')
def create_rivers() -> Response:
    """
    Create a new river
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              river_name:
                type: string
                description: Name of the river
              river_length:
                type: number
                description: Length of the river
              river_depth:
                type: number
                description: Depth of the river
              river_types_id:
                type: integer
                description: River type ID
              river_country:
                type: string
                description: Country where the river is located
    responses:
      201:
        description: River created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    rivers = Rivers.create_from_dto(content)
    rivers_controller.create(rivers)
    return make_response(jsonify(rivers.put_into_dto()), HTTPStatus.CREATED)


@rivers_bp.get('/<int:rivers_id>')
def get_rivers(rivers_id: int) -> Response:
    """
    Get river by ID
    ---
    parameters:
      - name: rivers_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river
    responses:
      200:
        description: River found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(rivers_controller.find_by_id(rivers_id)), HTTPStatus.OK)


@rivers_bp.put('/<int:rivers_id>')
def update_rivers(rivers_id: int) -> Response:
    """
    Update river by ID
    ---
    parameters:
      - name: rivers_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              river_name:
                type: string
              river_length:
                type: number
              river_depth:
                type: number
              river_types_id:
                type: integer
              river_country:
                type: string
    responses:
      200:
        description: River updated successfully
    """
    content = request.get_json()
    rivers = Rivers.create_from_dto(content)
    rivers_controller.update(rivers_id, rivers)
    return make_response("Rivers updated", HTTPStatus.OK)


@rivers_bp.patch('/<int:rivers_id>')
def patch_rivers(rivers_id: int) -> Response:
    """
    Partially update river by ID
    ---
    parameters:
      - name: rivers_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the river
    responses:
      200:
        description: River patched successfully
    """
    content = request.get_json()
    rivers_controller.patch(rivers_id, content)
    return make_response("Rivers updated", HTTPStatus.OK)


@rivers_bp.delete('/<int:rivers_id>')
def delete_rivers(rivers_id: int) -> Response:
    """
    Delete river by ID
    ---
    parameters:
      - name: rivers_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river
    responses:
      200:
        description: River deleted successfully
    """
    rivers_controller.delete(rivers_id)
    return make_response("Rivers deleted", HTTPStatus.OK)


@rivers_bp.get('/get-rivers-by-river-type/<int:river_type_id>')
def get_rivers_after_river_type(river_type_id: int) -> Response:
    """
    Get rivers by river type ID
    ---
    parameters:
      - name: river_type_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the river type
    responses:
      200:
        description: List of rivers with the specified river type
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(rivers_controller.get_rivers_after_river_type(river_type_id)), HTTPStatus.OK)


