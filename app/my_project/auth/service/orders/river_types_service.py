from lab4.app.my_project.auth.dao import river_types_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RiverTypesService(GeneralService):
    _dao = river_types_dao
