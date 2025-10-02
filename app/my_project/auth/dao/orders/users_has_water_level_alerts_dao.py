from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import UsersHasWaterLevelAlerts


class UsersHasWaterLevelAlertsDAO(GeneralDAO):
    _domain_type = UsersHasWaterLevelAlerts

    def get_users(self, users_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_users(:p1)"),
                                       {'p1': users_id}).mappings().all()
        return [dict(row) for row in result]

    def get_water_level_alerts(self, water_level_alerts_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_water_level_alerts(:p1)"),
                                       {'p1': water_level_alerts_id}).mappings().all()
        return [dict(row) for row in result]
