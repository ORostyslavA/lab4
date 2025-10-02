from typing import List

from lab4.app.my_project.auth.dao import rivers_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class RiversService(GeneralService):
    _dao = rivers_dao

    def get_rivers_after_river_type(self, river_type_id: int) -> List[object]:
        return self._dao.get_rivers_after_river_type(river_type_id)
