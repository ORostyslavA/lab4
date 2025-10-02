from lab4.app.my_project.auth.dao import meteorological_conditions_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class MeteorologicalConditionsService(GeneralService):
    _dao = meteorological_conditions_dao
