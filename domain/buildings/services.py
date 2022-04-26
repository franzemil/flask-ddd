from domain.buildings.entities import Building
from domain.buildings.repositories import BuildingRepository
from domain.buildings.valueobjects import Location


class BuildingSevice:
    def __init__(self, building_repository: BuildingRepository) -> None:
        self._repository = building_repository
    
    def save(self, description: str, location: Location) -> Building:
        to_save = Building('1', description, location, "")
        building = self._repository.save(to_save)

        return building