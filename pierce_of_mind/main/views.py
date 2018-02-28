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
