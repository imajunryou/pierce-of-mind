from flask import render_template
from . import main


@main.route("/")
def index():
    return render_template("index.html")

@main.route("/post")
def post():
    return render_template("post.html", title='title from db', url='video url from db', text='text from db')
