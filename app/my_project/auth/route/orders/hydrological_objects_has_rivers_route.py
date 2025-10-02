from http import HTTPStatus

from flask import Blueprint, jsonify, Response, request, make_response

from lab4.app.my_project.auth.controller import hydrological_objects_has_rivers_controller
from lab4.app.my_project.auth.domain import HydrologicalObjectsHasRivers

hydrological_objects_has_rivers_bp = Blueprint('hydrological_objects_has_rivers', __name__,
                                               url_prefix='/hydrological-objects-has-rivers')


@hydrological_objects_has_rivers_bp.get('')
def get_all_hydrological_objects_has_rivers() -> Response:
    """
    Get all hydrological-objects-has-rivers relations
    ---
    responses:
      200:
        description: List of all hydrological-objects-has-rivers relations
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hydrological_objects_has_rivers_controller.find_all()), HTTPStatus.OK)


@hydrological_objects_has_rivers_bp.post('')
def create_hydrological_objects_has_rivers() -> Response:
    """
    Create a new hydrological-objects-has-rivers relation
    ---
    requestBody:
      required: true
      content:
        application/json:
          schema:
            type: object
            properties:
              hydrological_objects_id:
                type: integer
                description: Hydrological object ID
              rivers_id:
                type: integer
                description: River ID
    responses:
      201:
        description: Relation created successfully
        content:
          application/json:
            schema:
              type: object
    """
    content = request.get_json()
    hydrological_objects_has_rivers = HydrologicalObjectsHasRivers.create_from_dto(content)
    hydrological_objects_has_rivers_controller.create(hydrological_objects_has_rivers)
    return make_response(jsonify(hydrological_objects_has_rivers.put_into_dto()), HTTPStatus.CREATED)


@hydrological_objects_has_rivers_bp.get('/<int:hydrological_objects_has_rivers_id>')
def get_hydrological_objects_has_rivers(hydrological_objects_has_rivers_id: int) -> Response:
    """
    Get hydrological-objects-has-rivers relation by ID
    ---
    parameters:
      - name: hydrological_objects_has_rivers_id
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
    return make_response(jsonify(hydrological_objects_has_rivers_controller.
                                 find_by_id(hydrological_objects_has_rivers_id)), HTTPStatus.OK)


@hydrological_objects_has_rivers_bp.put('/<int:hydrological_objects_has_rivers_id>')
def update_hydrological_objects_has_rivers(hydrological_objects_has_rivers_id: int) -> Response:
    """
    Update hydrological-objects-has-rivers relation by ID
    ---
    parameters:
      - name: hydrological_objects_has_rivers_id
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
              hydrological_objects_id:
                type: integer
              rivers_id:
                type: integer
    responses:
      200:
        description: Relation updated successfully
    """
    content = request.get_json()
    hydrological_objects_has_rivers = HydrologicalObjectsHasRivers.create_from_dto(content)
    hydrological_objects_has_rivers_controller.update(hydrological_objects_has_rivers_id,
                                                      hydrological_objects_has_rivers)
    return make_response("HydrologicalObjectsHasRivers updated", HTTPStatus.OK)


@hydrological_objects_has_rivers_bp.patch('/<int:hydrological_objects_has_rivers_id>')
def patch_hydrological_objects_has_rivers(hydrological_objects_has_rivers_id: int) -> Response:
    """
    Partially update hydrological-objects-has-rivers relation by ID
    ---
    parameters:
      - name: hydrological_objects_has_rivers_id
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
    hydrological_objects_has_rivers_controller.patch(hydrological_objects_has_rivers_id, content)
    return make_response("HydrologicalObjectsHasRivers updated", HTTPStatus.OK)


@hydrological_objects_has_rivers_bp.delete('/<int:hydrological_objects_has_rivers_id>')
def delete_hydrological_objects_has_rivers(hydrological_objects_has_rivers_id: int) -> Response:
    """
    Delete hydrological-objects-has-rivers relation by ID
    ---
    parameters:
      - name: hydrological_objects_has_rivers_id
        in: path
        required: true
        schema:
          type: integer
        description: Relation ID
    responses:
      200:
        description: Relation deleted successfully
    """
    hydrological_objects_has_rivers_controller.delete(hydrological_objects_has_rivers_id)
    return make_response("HydrologicalObjectsHasRivers deleted", HTTPStatus.OK)


@hydrological_objects_has_rivers_bp.get('/get-rivers/<int:rivers_id>')
def get_rivers(rivers_id: int) -> Response:
    """
    Get hydrological-objects-has-rivers relations by river ID
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
        description: List of relations for the river
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hydrological_objects_has_rivers_controller.get_rivers(rivers_id)), HTTPStatus.OK)


@hydrological_objects_has_rivers_bp.get('/get-hydrological-objects/<int:hydrological_objects_id>')
def get_hydrological_objects(hydrological_objects_id: int) -> Response:
    """
    Get hydrological-objects-has-rivers relations by hydrological object ID
    ---
    parameters:
      - name: hydrological_objects_id
        in: path
        required: true
        schema:
          type: integer
        description: Hydrological object ID
    responses:
      200:
        description: List of relations for the hydrological object
        content:
          application/json:
            schema:
              type: array
              items:
                type: object
    """
    return make_response(jsonify(hydrological_objects_has_rivers_controller.
                                 get_hydrological_objects(hydrological_objects_id)), HTTPStatus.OK)
