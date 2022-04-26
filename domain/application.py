from mimetypes import init

from domain.buildings.repositories import BuildingRepository
from domain.buildings.services import BuildingSevice


class Application:
    def __init__(self, building_repository: BuildingRepository) -> None:
        self._building_service = BuildingSevice(building_repository)

    @property
    def building_service(self):
        return self._building_service