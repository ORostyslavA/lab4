from __future__ import annotations
from typing import Dict, Any

from lab4.app.my_project import db
from lab4.app.my_project.auth.domain.i_dto import IDto


class MeasurementLocations(db.Model, IDto):
    __tablename__ = "measurement_locations"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True, nullable=False)
    location_name = db.Column(db.String(100), nullable=False)
    latitude = db.Column(db.Float, nullable=False)
    longitude = db.Column(db.Float, nullable=False)
    rivers_id = db.Column(db.Integer, db.ForeignKey('rivers.id'), nullable=False)
    rivers = db.relationship('Rivers', backref='measurement_locations')
    regions_id = db.Column(db.Integer, db.ForeignKey('regions.id'), nullable=False)
    regions = db.relationship('Regions', backref='measurement_locations')


    def __repr__(self) -> str:
        return (f"'{self.id}', {self.location_name}, {self.latitude}, {self.longitude}, {self.rivers_id}, "
                f"{self.regions_id} ")

    def put_into_dto(self) -> Dict[str, Any]:
        return {
            "id": self.id,
            "location_name": self.location_name,
            "latitude": self.latitude,
            "longitude": self.longitude,
            "rivers_id": self.rivers_id,
            "regions_id": self.regions_id,
        }

    @staticmethod
    def create_from_dto(dto_dict: Dict[str, Any]) -> MeasurementLocations:
        obj = MeasurementLocations(**dto_dict)
        return obj
