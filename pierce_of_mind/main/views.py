import sqlite3
from flask import g, render_template
from . import main


def connect_db():
    """Connect to the local database"""
    return sqlite3.connect("pierceofmind.db")


@main.route("/")
def index():
    g.db = connect_db()

    # Get all post titles and texts
    cursor = g.db.execute("""SELECT * FROM posts""")
    posts = [dict(title=row[1], video=row[2], text=row[3], author=row[4], pubDate=row[5], modDate=row[6]) for row in cursor.fetchall()]
    g.db.close()
    return render_template("index.html", posts=posts)


@main.route("about/")
def about():
    return render_template("about.html")


@main.route("post/<int:id>")
def post(id=None):
    g.db = connect_db()

    # Get post matching the given ID, if any
    query = 'SELECT * FROM posts WHERE rowid={id}'
    cursor = g.db.execute(query.format(id=id))
    rows = cursor.fetchall()

    row = rows[0] if rows else ["This post does not exist", "", ""]
    post = dict(title=row[1], video=row[2], text=row[3], author=row[4], pubDate=row[5], modDate=row[6])

    return render_template(
        "post.html",
        id=id,
        title=post["title"],
        url=post["video"],
        text=post["text"])
