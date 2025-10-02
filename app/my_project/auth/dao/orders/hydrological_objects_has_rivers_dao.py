from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import HydrologicalObjectsHasRivers


class HydrologicalObjectsHasRiversDAO(GeneralDAO):
    _domain_type = HydrologicalObjectsHasRivers

    def get_rivers(self, rivers_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_rivers(:p1)"),
                                       {'p1': rivers_id}).mappings().all()
        return [dict(row) for row in result]

    def get_hydrological_objects(self, hydrological_objects_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_hydrological_objects(:p1)"),
                                       {'p1': hydrological_objects_id}).mappings().all()
        return [dict(row) for row in result]
