from dataclasses import dataclass

from common.domain import Entity
from domain.buildings.valueobjects import Location

@dataclass
class Building(Entity):
    id: str
    description: str
    location: Location
    imageUrl: str