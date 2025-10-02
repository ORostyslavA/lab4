from typing import List

from lab4.app.my_project.auth.service import hydrological_objects_has_rivers_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class HydrologicalObjectsHasRiversController(GeneralController):
    _service = hydrological_objects_has_rivers_service

    def get_hydrological_objects(self, hydrological_objects_id: int) -> List[object]:
        return self._service.get_hydrological_objects(hydrological_objects_id)

    def get_rivers(self, rivers_id: int) -> List[object]:
        return self._service.get_rivers(rivers_id)
