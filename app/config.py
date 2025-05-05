import os

basedir = os.path.abspath(os.path.dirname(__file__))
default_database_uri = 'sqlite:///' + os.path.join(basedir, 'app.db')

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'amber_pearl_latte_is_the_best'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or default_database_uri