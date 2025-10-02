from typing import List

from lab4.app.my_project.auth.dao import water_level_alerts_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WaterLevelAlertsService(GeneralService):
    _dao = water_level_alerts_dao

    def get_water_level_alerts_after_measurement_locations(self, measurement_locations_id: int) -> List[object]:
        return self._dao.get_water_level_alerts_after_measurement_locations(measurement_locations_id)
