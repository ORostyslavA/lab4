from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import WaterLevelsHasMeteorologicalConditions


class WaterLevelsHasMeteorologicalConditionsDAO(GeneralDAO):
    _domain_type = WaterLevelsHasMeteorologicalConditions

    def get_water_levels(self, water_levels_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_water_levels(:p1)"),
                                       {'p1': water_levels_id}).mappings().all()
        return [dict(row) for row in result]

    def get_meteorological_conditions(self, meteorological_conditions_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_meteorological_conditions(:p1)"),
                                       {'p1': meteorological_conditions_id}).mappings().all()
        return [dict(row) for row in result]
