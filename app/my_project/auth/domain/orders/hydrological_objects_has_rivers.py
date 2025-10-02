from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class HydrologicalObjectsHasRivers(db.Model, IDto):
    __tablename__ = "hydrological_objects_has_rivers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    hydrological_objects_id = db.Column(db.Integer, db.ForeignKey('hydrological_objects.id'), nullable=False)
    hydrological_objects = db.relationship("HydrologicalObjects", backref="hydrological_objects_has_rivers")
    rivers_id = db.Column(db.Integer, db.ForeignKey('rivers.id'), nullable=False)
    rivers = db.relationship("Rivers", backref="hydrological_objects_has_rivers")

    def __repr__(self) -> str:
        return f"'{self.id}', {self.hydrological_objects_id}, {self.rivers_id} "

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "hydrological_objects_id": self.hydrological_objects.id,
            "rivers_id": self.rivers.id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> HydrologicalObjectsHasRivers:
        obj = HydrologicalObjectsHasRivers(**dto_dict)
        return obj
