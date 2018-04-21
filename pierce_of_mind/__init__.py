import os

from flask import Flask
from flask_bcrypt import Bcrypt
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

from .config import config_by_name


app = Flask(__name__)
app.config.from_object(config_by_name[
    os.getenv("PIERCE_OF_MIND_ENV") or "dev"
])
app.config.from_envvar("PIERCE_OF_MIND_CONFIG")

bcrypt = Bcrypt(app)
db = SQLAlchemy(app)

# Imports the main page, and error pages
from .main import main as main_blueprint
app.register_blueprint(main_blueprint, url_prefix="/")

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

@login_manager.user_loader
def load_user(userid):
    return main_blueprint.User.query.filter(User.id==userid).first()
