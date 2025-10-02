from typing import List

from lab4.app.my_project.auth.dao import hydrological_objects_has_rivers_dao
from lab4.app.my_project.auth.service.general_service import GeneralService


class HydrologicalObjectsHasRiversService(GeneralService):
    _dao = hydrological_objects_has_rivers_dao

    def get_hydrological_objects(self, hydrological_objects_id: int) -> List[object]:
        return self._dao.get_hydrological_objects(hydrological_objects_id)

    def get_rivers(self, rivers_id: int) -> List[object]:
        return self._dao.get_rivers(rivers_id)
