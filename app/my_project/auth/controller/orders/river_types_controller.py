from lab4.app.my_project.auth.service import river_types_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class RiverTypesController(GeneralController):
    _service = river_types_service
