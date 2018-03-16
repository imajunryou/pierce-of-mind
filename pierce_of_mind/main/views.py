from flask import render_template
from . import main


@main.route("/")
def index():
    posts = [
        {
            "title": "Hello world",
            "video": 'https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2Fmathew.s.pierce.5%2Fvideos%2F10214268153165023%2F&show_text=0&width=560',
            "text": "I am a text"
        },
        {
            "title": "I am a second post!",
            "video": 'https://www.youtube.com/embed/UO3h4FBLWqY',
            "text": "I am more text"
        }
    ]
    return render_template("index.html", posts=posts)


@main.route("about/")
def about():
    return render_template("about.html")


@main.route("post/<id>")
def post(id=None):
    return render_template(
        "post.html",
        id=id,
        title='title from db',
        url='video url from db',
        text='text from db')
