from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class MeteorologicalConditions(db.Model, IDto):
    __tablename__ = "meteorological_conditions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    condition_type = db.Column(db.String(150), nullable=False)
    condition_description = db.Column(db.String(150), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.condition_type}, {self.condition_description}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "condition_type": self.condition_type,
            "condition_description": self.condition_description,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MeteorologicalConditions:
        obj = MeteorologicalConditions(**dto_dict)
        return obj
