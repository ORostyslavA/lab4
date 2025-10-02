from lab4.app.my_project.auth.service import meteorological_conditions_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class MeteorologicalConditionsController(GeneralController):
    _service = meteorological_conditions_service
