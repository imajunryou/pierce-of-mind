from flask import render_template
from . import main
from .models import Post


@main.route("/")
def index():
    # Get all post titles and texts
    p = Post.query.get(1)
    posts = [dict(id=p.id, title=p.title, video=p.video, text=p.content)]
    return render_template("index.html", posts=posts)


@main.route("about/")
def about():
    return render_template("about.html")


@main.route("post/<int:id>")
def post(id=None):
    # Get post matching the given ID, if any
    p = Post.query.get(id)
    if p is None:
        post = dict(title="This post does not exist", video="", text="")
    else:
        post = dict(title=p.title, video=p.video, text=p.content)

    return render_template(
        "post.html",
        id=id,
        title=post["title"],
        url=post["video"],
        text=post["text"])
