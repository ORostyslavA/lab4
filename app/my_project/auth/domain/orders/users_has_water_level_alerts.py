from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class UsersHasWaterLevelAlerts(db.Model, IDto):
    __tablename__ = "users_has_water_level_alerts"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    users_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    users = db.relationship("Users", backref="has_water_level_alerts")
    water_level_alerts_id = db.Column(db.Integer, db.ForeignKey("water_level_alerts.id"), nullable=False)
    water_level_alerts = db.relationship("WaterLevelAlerts", backref="has_water_level_alerts")

    def __repr__(self) -> str:
        return f"'{self.id}', {self.users_id}, {self.water_level_alerts_id}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "users_id": self.users_id,
            "water_level_alerts_id": self.water_level_alerts_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> UsersHasWaterLevelAlerts:
        obj = UsersHasWaterLevelAlerts(**dto_dict)
        return obj
