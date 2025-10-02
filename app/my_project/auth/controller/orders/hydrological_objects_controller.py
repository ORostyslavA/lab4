from lab4.app.my_project.auth.service import hydrological_objects_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class HydrologicalObjectsController(GeneralController):
    _service = hydrological_objects_service
