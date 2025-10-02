from typing import List

from lab4.app.my_project.auth.service import water_level_alerts_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class WaterLevelAlertsController(GeneralController):
    _service = water_level_alerts_service

    def get_water_level_alerts_after_measurement_locations(self, measurement_locations_id: int) -> List[object]:
        return self._service.get_water_level_alerts_after_measurement_locations(measurement_locations_id)