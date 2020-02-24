import os


class BaseConfig(object):
    DEBUG = False
    TESTING = False

class DevelopmentConfig(BaseConfig):
    DEBUG = True
    TESTING = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://fordwh444@localhost/tesseract'


class TestingConfig(BaseConfig):
    DEBUG = False
    TESTING = True

class ProductionConfig(BaseConfig):
    DEBUG = False
    TESTING = False
    SQLALCHEMY_DATABASE_URI = \
    'postgresql+psycopg2://{user}:{passwd}@{host}:{port}/{db}'.format(
        user=os.environ['DBUSER'],
        passwd=os.environ['DBPASS'],
        host=os.environ['DBHOST'],
        port=os.environ['DBPORT'],
        db=os.environ['DBNAME'])
