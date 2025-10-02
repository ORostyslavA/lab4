from typing import List

from lab4.app.my_project.auth.dao import water_levels_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WaterLevelsService(GeneralService):
    _dao = water_levels_dao

    def get_water_levels_after_measurement_locations(self, measurement_locations_id: int) -> List[object]:
        return self._dao.get_water_levels_after_measurement_locations(measurement_locations_id)