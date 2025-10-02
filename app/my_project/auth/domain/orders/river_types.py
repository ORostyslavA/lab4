from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class RiverTypes(db.Model, IDto):

    __tablename__ = "river_types"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    type_description = db.Column(db.String(255), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.type_description}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "type_description": self.type_description,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> RiverTypes:
        obj = RiverTypes(**dto_dict)
        return obj
