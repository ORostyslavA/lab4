from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import MeasurementLocations


class MeasurementLocationsDAO(GeneralDAO):
    _domain_type = MeasurementLocations

    def get_measurement_locations_after_rivers(self, rivers_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_measurement_locations_after_rivers(:p1)"),
                                       {'p1': rivers_id}).mappings().all()
        return [dict(row) for row in result]

    def get_measurement_locations_after_regions(self, regions_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_measurement_locations_after_regions(:p1)"),
                                       {'p1': regions_id}).mappings().all()
        return [dict(row) for row in result]
