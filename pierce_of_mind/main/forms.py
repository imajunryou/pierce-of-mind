from flask_wtf import FlaskForm
from wtforms import BooleanField, PasswordField, StringField, \
    SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length, Optional, URL

from .models import User
from ..util import Unique


class PostForm(FlaskForm):
    title = StringField(
        "Title", validators=[
            DataRequired(message="The post must not have an empty title")
        ]
    )
    publish_date = DateField("Publish Date", validators=[
        DataRequired(
            message="You must indicate when this post should be made public"
        )
    ])
    modify_date = DateField("Modify Date")
    video = StringField("Video Link", validators=[Optional(), URL()])
    content = TextAreaField("Post Content", validators=[Optional()])
    author = StringField("Author", validators=[
        DataRequired(message="You must indicate who the author is"),
        Email(message="The author should be an email")
    ])
    private = BooleanField("Keep Post Unpublished")
    submit = SubmitField("Submit")


class LoginForm(FlaskForm):
    username = StringField("User Name", validators=[
        DataRequired(
            message="You must enter a valid user name"
        ), Email(message="Your username must be an email")
    ])
    password = PasswordField("Password", validators=[
        DataRequired(
            message="You must enter a password"
        )
    ])
    submit = SubmitField("Log In")


class SignupForm(FlaskForm):
    first_name = StringField("First Name", validators=[
        DataRequired(message="You must enter a first name"),
        Length(max=50)
    ])
    last_name = StringField("Last Name", validators=[
        DataRequired(message="You must enter a last name"),
        Length(max=50)
    ])
    email = StringField("Email Address", validators=[
        DataRequired(message="You must enter an email address"),
        Email(message="You must enter a valid email address"),
        Unique(
            User,
            User.email,
            message="There is already an account with that email."
        )
    ])
    password = PasswordField("Password", validators=[
        DataRequired(message="You must enter a password")
    ])
    submit = SubmitField("Create New User")
