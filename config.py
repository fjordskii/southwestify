import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = os.getenv("DATABASE_URL", "sqlite://")


class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    ENV = 'development'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
