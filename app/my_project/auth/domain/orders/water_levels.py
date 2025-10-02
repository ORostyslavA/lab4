from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class WaterLevels(db.Model, IDto):

    __tablename__ = "water_levels"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    water_level_value = db.Column(db.Float, nullable=False)
    measurement_locations_id = db.Column(db.Integer, db.ForeignKey("measurement_locations.id"), nullable=False)
    measurement_locations = db.relationship("MeasurementLocations", backref="water_levels")
    start_date = db.Column(db.Date, nullable=False)
    end_date = db.Column(db.Date, nullable=False)

    def __repr__(self) -> str:
        return (f"'{self.id}', {self.water_level_value}, {self.measurement_locations_id}, {self.start_date}, "
                f"{self.end_date}")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "water_level_value": self.water_level_value,
            "measurement_locations_id": self.measurement_locations_id,
            "start_date": self.start_date,
            "end_date": self.end_date,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WaterLevels:
        obj = WaterLevels(**dto_dict)
        return obj
