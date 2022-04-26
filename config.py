from typing import Union


class BaseConfig:
    DEBUG = True

class DevelopmentConfig(BaseConfig):
    DEBUG = True

class ProductionConfig(BaseConfig):
    DEBUG = False


def get_config(name: Union['dev', 'prod']):
    if  name == 'dev':
        return DevelopmentConfig
    else:
        return ProductionConfig