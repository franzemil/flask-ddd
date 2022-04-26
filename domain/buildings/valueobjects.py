from common.domain import ValueObject
from dataclasses import dataclass

@dataclass(frozen=True)
class Location(ValueObject):
    lat: float
    long: float