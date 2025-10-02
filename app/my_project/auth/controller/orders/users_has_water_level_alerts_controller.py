from typing import List

from lab4.app.my_project.auth.service import user_has_water_level_alerts_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class UserHasWaterLevelAlertsController(GeneralController):

    _service = user_has_water_level_alerts_service

    def get_users(self, users_id: int) -> List[object]:
        return self._service.get_users(users_id)

    def get_water_level_alerts(self, water_level_alerts_id: int) -> List[object]:
        return self._service.get_water_level_alerts(water_level_alerts_id)
