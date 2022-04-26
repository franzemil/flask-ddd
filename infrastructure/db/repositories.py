from sqlalchemy.orm import Session

from domain.buildings.entities import Building
from domain.buildings.repositories import BuildingRepository

class SqliteBuildingRepository(BuildingRepository):
    def __init__(self, session: Session) -> None:
        self._session = session

    def save(self, building: Building) -> Building:
        self._session.add(building)
        self._session.commit()
        return building
        