from flask import flash, render_template, request
from . import main
from .models import Post


@main.route("/")
def index():
    # Get all post titles and texts
    ps = Post.query.all()
    posts = []
    for p in ps:
        posts.append(
            dict(id=p.id, title=p.title, video=p.video, text=p.content)
        )
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


@main.route("edit/", methods=['GET', 'POST'])
def edit():
    if request.method == 'POST':
        # Edit the given post
        flash("Successfully edited the post")
    return render_template("edit.html", heading="Edit Existing Post")

@main.route("new/", methods=['GET', 'POST'])
def new():
    if request.method == 'POST':
        flash("Successfully created a new post")
    return render_template("edit.html", heading="Create New Post")


@main.route("archive/")
def archive():
    ps = Post.query.all()
    posts = []
    print("PS Size: " + str(len(ps)))
    for p in ps:

        posts.append(dict(id=p.id, title=p.title))
    return render_template("archive.html", posts=posts)
