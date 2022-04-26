from xml.dom.minidom import Entity
from sqlalchemy import Column, Float, String
from sqlalchemy.orm import declarative_base

from domain.buildings.entities import Building
from domain.buildings.valueobjects import Location


Base = declarative_base()


class BuildingModel(Base):
    __tablename__ = 'building'

    id = Column(String(25), primary_key=True)
    description = Column(String(200))
    image = Column(String(200))
    lat = Column(Float(5))
    log = Column(Float(5))

    def to_entity(self) -> Building:
        return Building(
            id=self.id,
            description=self.description,
            image=self.images,
            location=Location(self.lat, self.log)
        )
