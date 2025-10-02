from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import regions_controller
from lab4.app.my_project.auth.domain import Regions

regions_bp = Blueprint('regions', __name__, url_prefix='/regions')


@regions_bp.get('')
def get_all_regions() -> Response:
    """
    Get all regions
    ---
    responses:
      200:
        description: List of all regions
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(regions_controller.find_all()), HTTPStatus.OK)


@regions_bp.post('')
def create_regions() -> Response:
    """
    Create a new region
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              region_name:
                type: string
                description: Name of the region
              country:
                type: string
                description: Country of the region
    responses:
      201:
        description: Region created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    regions = Regions.create_from_dto(content)
    regions_controller.create(regions)
    return make_response(jsonify(regions.put_into_dto()), HTTPStatus.CREATED)


@regions_bp.get('/<int:regions_id>')
def get_regions(regions_id: int) -> Response:
    """
    Get region by ID
    ---
    parameters:
      - name: regions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the region
    responses:
      200:
        description: Region found
        content:
          application/json:
            schema:
              type: object
    """
    return make_response(jsonify(regions_controller.find_by_id(regions_id)), HTTPStatus.OK)


@regions_bp.put('/<int:regions_id>')
def update_regions(regions_id: int) -> Response:
    """
    Update region by ID
    ---
    parameters:
      - name: regions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the region
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              region_name:
                type: string
              country:
                type: string
    responses:
      200:
        description: Region updated successfully
    """
    content = request.get_json()
    regions = Regions.create_from_dto(content)
    regions_controller.update(regions_id, regions)
    return make_response("Regions updated", HTTPStatus.OK)


@regions_bp.patch('/<int:regions_id>')
def patch_regions(regions_id: int) -> Response:
    """
    Partially update region by ID
    ---
    parameters:
      - name: regions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the region
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            description: Fields to update in the region
    responses:
      200:
        description: Region patched successfully
    """
    content = request.get_json()
    regions_controller.patch(regions_id, content)
    return make_response("Regions updated", HTTPStatus.OK)


@regions_bp.delete('/<int:regions_id>')
def delete_rivers(regions_id: int) -> Response:
    """
    Delete region by ID
    ---
    parameters:
      - name: regions_id
        in: path
        required: true
        schema:
          type: integer
        description: ID of the region
    responses:
      200:
        description: Region deleted successfully
    """
    regions_controller.delete(regions_id)
    return make_response("Regions deleted", HTTPStatus.OK)




