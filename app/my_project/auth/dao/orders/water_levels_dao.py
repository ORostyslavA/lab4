from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import WaterLevels


class WaterLevelsDAO(GeneralDAO):
    _domain_type = WaterLevels

    def get_water_levels_after_measurement_locations(self, measurement_locations_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_water_levels_after_measurement_locations(:p1)"),
                                       {'p1': measurement_locations_id}).mappings().all()
        return [dict(row) for row in result]
