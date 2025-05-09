from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from app.config import Config

application = Flask(__name__)
# application.config['SECRET_KEY'] = 'amber_pearl_latte_is_the_best'
application.config.from_object(Config)
db = SQLAlchemy(application)
migrate = Migrate(application, db)
login = LoginManager(application)
login.login_view = 'login'

from app import routes, models