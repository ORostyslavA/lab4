from lab4.app.my_project.auth.service import regions_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class RegionsController(GeneralController):
    _service = regions_service
