
from flask import Blueprint

blueprint = Blueprint('main', __name__)

from app import models, routes