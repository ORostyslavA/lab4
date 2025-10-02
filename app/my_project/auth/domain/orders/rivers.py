from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Rivers(db.Model, IDto):

    __tablename__ = "rivers"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    river_name = db.Column(db.String(100), nullable=False)
    river_length = db.Column(db.Float, nullable=False)
    river_depth = db.Column(db.Float, nullable=False)
    river_country = db.Column(db.String(100), nullable=False)
    river_types_id = db.Column(db.Integer, db.ForeignKey('river_types.id'), nullable=False)
    river_types = db.relationship('RiverTypes', backref='rivers')

    def __repr__(self) -> str:
        return (f"'{self.id}', {self.river_name}, {self.river_length}, {self.river_depth}, "
                f"{self.river_country}")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "river_name": self.river_name,
            "river_length": self.river_length,
            "river_depth": self.river_depth,
            "river_types_id": self.river_types_id,
            "river_country": self.river_country,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Rivers:
        obj = Rivers(**dto_dict)
        return obj
