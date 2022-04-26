from abc import ABC, abstractmethod
from domain.buildings.entities import Building


class BuildingRepository(ABC):
    @abstractmethod
    def save(building: Building) -> Building:
        raise NotImplementedError

    def get_paged(filter: str, pageSize: int, pageNumber: int):
        raise NotImplementedError