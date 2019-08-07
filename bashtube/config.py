import os


class LocalConfig:
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
    DEBUG = True
    DEVELOPEMENT = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = os.environ.get('SECRET_KEY')
    CACHE_TYPE = 'simple'


class ProductionConfig:
    DEBUG = False
    PRODUCTION = True
    CACHE_TYPE = 'simple'
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL')
