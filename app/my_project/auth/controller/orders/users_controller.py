from lab4.app.my_project.auth.service import users_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class UsersController(GeneralController):
    _service = users_service
