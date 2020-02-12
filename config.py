import os

class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://fordwh44@localhost/pyschedule'

class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
