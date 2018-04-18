import os

from .config import config_by_name

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config.from_object(config_by_name[
    os.getenv("PIERCE_OF_MIND_ENV") or "dev"
])
app.config.from_envvar("PIERCE_OF_MIND_CONFIG")

db = SQLAlchemy(app)

# Imports the main page, and error pages
from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix="/")
