from lab4.app.my_project.auth.dao import users_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class UsersService(GeneralService):
    _dao = users_dao
