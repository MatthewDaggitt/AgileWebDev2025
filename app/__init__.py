from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

db = SQLAlchemy()
login = LoginManager()
login.login_view = 'login'

def create_application(config):
    application = Flask(__name__)
    application.config.from_object(config)

    db.init_app(application)
    login.init_app(application)

    from app.blueprints import blueprint
    application.register_blueprint(blueprint)

    return application