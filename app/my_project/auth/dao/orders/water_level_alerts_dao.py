from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import WaterLevelAlerts


class WaterLevelAlertsDAO(GeneralDAO):
    _domain_type = WaterLevelAlerts

    def get_water_level_alerts_after_measurement_locations(self, measurement_locations_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_water_level_alerts_after_measurement_locations(:p1)"),
                                       {'p1': measurement_locations_id}).mappings().all()
        return [dict(row) for row in result]
