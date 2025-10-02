from typing import List

from lab4.app.my_project.auth.dao import user_has_water_level_alerts_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class UserHasWaterLevelAlertsService(GeneralService):
    _dao = user_has_water_level_alerts_dao

    def get_users(self, users_id: int) -> List[object]:
        return self._dao.get_users(users_id)

    def get_water_level_alerts(self, water_level_alerts_id: int) -> List[object]:
        return self._dao.get_water_level_alerts(water_level_alerts_id)
