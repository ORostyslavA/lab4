from typing import List

from lab4.app.my_project.auth.service import water_levels_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class WaterLevelsController(GeneralController):
    _service = water_levels_service

    def get_water_levels_after_measurement_locations(self, measurement_locations_id: int) -> List[object]:
        return self._service.get_water_levels_after_measurement_locations(measurement_locations_id)
