from lab4.app.my_project.auth.dao import regions_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RegionsService(GeneralService):
    _dao = regions_dao
