from flask import Flask

from config import get_config

from domain.application import Application
from domain.buildings.valueobjects import Location
from infrastructure.db.db import create_session
from infrastructure.db.repositories import SqliteBuildingRepository


def create_app(config='prod'):
    app = Flask(__name__)
    app.config.from_object(get_config(config))

    session = create_session()

    sqlite_building_repository = SqliteBuildingRepository(session)

    demo_domain = Application(sqlite_building_repository)

    @app.route('/')
    def add_buiding():
        demo_domain.building_service.save('This is the Repository', Location(1, 1))
        return 'Hello world gaaa!!'

    return app


if __name__ == '__main__':
    app = create_app('dev')
    app.run()
