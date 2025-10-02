from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class WaterLevelsHasMeteorologicalConditions(db.Model, IDto):
    __tablename__ = "water_levels_has_meteorological_conditions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    water_levels_id = db.Column(db.Integer, db.ForeignKey("water_levels.id"), nullable=False)
    water_levels = db.relationship("WaterLevels", backref="water_levels_has_meteorological_conditions")
    meteorological_conditions_id = db.Column(db.Integer, db.ForeignKey("meteorological_conditions.id"), nullable=False)
    meteorological_conditions = db.relationship("MeteorologicalConditions",
                                                backref="water_levels_has_meteorological_conditions")

    def __repr__(self) -> str:
        return f"'{self.id}', {self.water_levels_id}, {self.meteorological_conditions_id} "

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "water_levels_id": self.water_levels_id,
            "meteorological_conditions_id": self.meteorological_conditions_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WaterLevelsHasMeteorologicalConditions:
        obj = WaterLevelsHasMeteorologicalConditions(**dto_dict)
        return obj
