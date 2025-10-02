from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class HydrologicalObjects(db.Model, IDto):
    __tablename__ = "hydrological_objects"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    object_type = db.Column(db.String(100), nullable=False)
    object_description = db.Column(db.Text, nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.object_type}, {self.object_description}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "object_type": self.object_type,
            "object_description": self.object_description,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HydrologicalObjects:
        obj = HydrologicalObjects(**dto_dict)
        return obj
