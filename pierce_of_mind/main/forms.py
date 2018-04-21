from urllib.parse import urlparse, urljoin
from flask import request, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import BooleanField, HiddenField, PasswordField, StringField, SubmitField, TextAreaField
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Email, Length, Optional, URL

from .models import User
from ..util import Unique


def is_safe_url(target):
    ref_url = urlparse(request.host_url)
    test_url = urlparse(urljoin(request.host_url, target))
    print("Checking the safety of the target: " + target)
    return test_url.scheme in ('http', 'https') and \
        ref_url.netloc == test_url.netloc

def get_redirect_target():
    for target in request.args.get('next'), request.referrer:
        print("Checking target: " + str(target))
        if not target:
            continue
        if is_safe_url(target):
            print("Found safe redirect target: " + target)
            return target


class PostForm(FlaskForm):
    title = StringField(
        "Title", validators=[
            DataRequired(message="The post must not have an empty title")
        ]
    )
    publish_date = DateField("Publish Date", validators=[
            DataRequired(message="You must indicate when this post should be made public")
        ]
    )
    modify_date = DateField("Modify Date")
    video = StringField("Video Link", validators=[Optional(), URL()])
    content = TextAreaField("Post Content", validators=[Optional()])
    author = StringField("Author", validators=[
            DataRequired(message="You must indicate who the author is"),
            Email(message="The author should be an email")
        ]
    )
    private = BooleanField("Keep Post Unpublished")
    submit = SubmitField("Submit")


class RedirectForm(FlaskForm):
    next = HiddenField()

    def __init__(self, *args, **kwargs):
        super(RedirectForm, self).__init__(*args, **kwargs)
        if not self.next.data:
            print("next data was empty, grabbing a new one")
            self.next.data = get_redirect_target() or ""

    def redirect(self, endpoint='main.index', **values):
        print("Redirecting through the form")
        if is_safe_url(self.next.data):
            print("Next data is safe: " + self.next.data)
            return redirect(self.next.data)
        target = get_redirect_target()
        return redirect(target or url_for(endpoint, **values))


class LoginForm(RedirectForm):
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
