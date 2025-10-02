from typing import List

from lab4.app.my_project.auth.service import rivers_service
from lab4.app.my_project.auth.controller.general_controller import GeneralController


class RiversController(GeneralController):
    _service = rivers_service

    def get_rivers_after_river_type(self, river_type_id: int) -> List[object]:
        return self._service.get_rivers_after_river_type(river_type_id)