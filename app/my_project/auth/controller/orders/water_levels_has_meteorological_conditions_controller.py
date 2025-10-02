from typing import List

from lab4.app.my_project.auth.service import water_levels_has_meteorological_conditions_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class WaterLevelsHasMeteorologicalConditionsController(GeneralController):
    _service = water_levels_has_meteorological_conditions_service

    def get_water_levels(self, water_levels_id: int) -> List[object]:
        return self._service.get_water_levels(water_levels_id)

    def get_meteorological_conditions(self, meteorological_conditions_id: int) -> List[object]:
        return self._service.get_meteorological_conditions(meteorological_conditions_id)
