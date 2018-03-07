from flask import render_template
from . import main


@main.route("/")
def index():
    return render_template("index.html")


@main.route("post/<id>")
def post(id=None):
    return render_template("post.html", id=id, title='title from db', url='video url from db', text='text from db')
