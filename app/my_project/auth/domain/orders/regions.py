from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Regions(db.Model, IDto):
    __tablename__ = "regions"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    region_name = db.Column(db.String(100), nullable=False)
    country = db.Column(db.String(100), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.region_name}, {self.country} "

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "region_name": self.region_name,
            "country": self.country,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Regions:
        obj = Regions(**dto_dict)
        return obj
