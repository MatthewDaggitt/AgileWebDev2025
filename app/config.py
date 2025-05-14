import os

basedir = os.path.abspath(os.path.dirname(__file__))
default_database_uri = 'sqlite:///' + os.path.join(basedir, 'app.db')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY')

class DeploymentConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or default_database_uri

class TestingConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'sqlite:///:memory'
