from typing import List, Dict, Any

import sqlalchemy

from lab4.app.my_project.auth.dao.general_dao import GeneralDAO
from lab4.app.my_project.auth.domain import Rivers


class RiversDAO(GeneralDAO):
    _domain_type = Rivers

    def get_rivers_after_river_type(self, river_type_id: int) -> List[Dict[str, Any]]:
        result = self._session.execute(sqlalchemy.text("CALL get_rivers_after_river_type(:p1)"),
                                       {'p1': river_type_id}).mappings().all()
        return [dict(row) for row in result]
