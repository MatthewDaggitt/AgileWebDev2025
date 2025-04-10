from flask import Flask, render_template

application = Flask(__name__)
application.config['SECRET_KEY'] = 'amber-pearl-latte-is-the-best'

from app import routes