from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class WaterLevelAlerts(db.Model, IDto):
    __tablename__ = "water_level_alerts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    water_level = db.Column(db.Float, nullable=False)
    alert_level = db.Column(db.Integer, nullable=False)
    alert_date = db.Column(db.Date, nullable=False)
    measurement_locations_id = db.Column(db.Integer, db.ForeignKey('measurement_locations.id'), nullable=False)
    measurement_locations = db.relationship('MeasurementLocations', backref='water_level_alerts')

    def __repr__(self) -> str:
        return (f"'{self.id}', {self.water_level}, {self.alert_level}, {self.alert_date}, "
                f"{self.measurement_locations_id}")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "water_level": self.water_level,
            "alert_level": self.alert_level,
            "alert_date": self.alert_date,
            "measurement_locations_id": self.measurement_locations_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> WaterLevelAlerts:
        obj = WaterLevelAlerts(**dto_dict)
        return obj
