from typing import List

from lab4.app.my_project.auth.dao import measurement_locations_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class MeasurementLocationsService(GeneralService):
    _dao = measurement_locations_dao

    def get_measurement_locations_after_rivers(self, rivers_id: int) -> List[object]:
        return self._dao.get_measurement_locations_after_rivers(rivers_id)

    def get_measurement_locations_after_regions(self, regions_id: int) -> List[object]:
        return self._dao.get_measurement_locations_after_regions(regions_id)
