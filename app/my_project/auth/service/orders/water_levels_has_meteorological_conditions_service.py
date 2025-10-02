from typing import List

from lab4.app.my_project.auth.dao import water_levels_has_meteorological_conditions_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class WaterLevelsHasMeteorologicalConditionsService(GeneralService):
    _dao = water_levels_has_meteorological_conditions_dao

    def get_water_levels(self, water_levels_id: int) -> List[object]:
        return self._dao.get_water_levels(water_levels_id)

    def get_meteorological_conditions(self, meteorological_conditions_id: int) -> List[object]:
        return self._dao.get_meteorological_conditions(meteorological_conditions_id)

