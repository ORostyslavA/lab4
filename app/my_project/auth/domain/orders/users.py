from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class Users(db.Model, IDto):
    __tablename__ = "users"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    user_name = db.Column(db.String(50), nullable=False)
    user_surname = db.Column(db.String(50), nullable=False)
    user_email = db.Column(db.String(50), nullable=False)

    def __repr__(self) -> str:
        return f"'{self.id}', {self.user_name}, {self.user_surname}, {self.user_email}"

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "user_name": self.user_name,
            "user_surname": self.user_surname,
            "user_email": self.user_email,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> Users:
        obj = Users(**dto_dict)
        return obj
