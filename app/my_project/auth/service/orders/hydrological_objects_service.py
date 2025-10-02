from lab4.app.my_project.auth.dao import hydrological_objects_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class HydrologicalObjectsService(GeneralService):
    _dao = hydrological_objects_dao
