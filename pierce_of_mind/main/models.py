from datetime import datetime
from .. import db


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
    title = db.Column(db.String(256))
    video = db.Column(db.String(2048), default=None)
    content = db.Column(db.String(10000))
    author = db.Column(db.String(128))
    pub_date = db.Column(db.Date(), default=datetime.utcnow())
    mod_date = db.Column(db.Date(), default=None)

    def __repr__(self):
        return "Post #{}: {} by {}".format(
            self.id, self.title, self.author
        )
