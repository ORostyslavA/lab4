from typing import List

from lab4.app.my_project.auth.service import measurement_locations_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class MeasurementLocationsController(GeneralController):
    _service = measurement_locations_service

    def get_measurement_locations_after_rivers(self, rivers_id: int) -> List[object]:
        return self._service.get_measurement_locations_after_rivers(rivers_id)

    def get_measurement_locations_after_regions(self, regions_id: int) -> List[object]:
        return self._service.get_measurement_locations_after_regions(regions_id)
