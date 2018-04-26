from datetime import datetime
from flask_login import UserMixin
from sqlalchemy.ext.hybrid import hybrid_property
from .. import bcrypt, db


class Post(db.Model):
    """Blog Post

    Fields:
    id - auto-incremented primary key
    title - String, max length of 256
    video - String (url), max length of 2048, defaults to None
    content - String, max length of 10,000
    author - String (email), max length of 128
    pub_date - Date, defaults to the current time
    mod_date - Date, defaults to None
    """
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(256), nullable=False)
    video = db.Column(db.String(2048), default=None)
    content = db.Column(db.String(10000))
    author = db.Column(db.String(128), nullable=False)
    pub_date = db.Column(db.Date(), default=datetime.utcnow())
    private = db.Column(db.Boolean(), nullable=False)

    def __repr__(self):
        return "Post #{}: {} by {}".format(
            self.id, self.title, self.author
        )


class User(UserMixin, db.Model):
    """ Blog user"""
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    email = db.Column(db.String(120), unique=True, nullable=False)
    first_name = db.Column(db.String(50), nullable=False)
    last_name = db.Column(db.String(50), nullable=False)
    confirmed = db.Column(db.Boolean(), nullable=False, default=False)
    password = db.Column(db.String(128))

    # @hybrid_property
    # def password(self):
    #     return self._password

    # @password.setter
    # def _set_password(self, plaintext):
    #     self._password = bcrypt.generate_password_hash(plaintext)

    def __init__(self, first_name, last_name, email, plaintext):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.password = bcrypt.generate_password_hash(plaintext)

    def __repr__(self):
        return "User {fn} {ln}: {em}".format(
            fn=self.first_name, ln=self.last_name, em=self.email
        )

    def is_correct_password(self, plaintext):
        return bcrypt.check_password_hash(self.password, plaintext)
