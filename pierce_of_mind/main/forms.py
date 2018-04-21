from flask_wtf import Form
from wtforms import StringField, DateField, TextAreaField
from wtforms.validators import DataRequired, Email


class NewPostForm(Form):
    title = StringField("Title", validators=[DataRequired()])
    publish_date = DateField("Publish", validators=[DataRequired()])
    video = StringField("Video")
    content = TextAreaField("Content")
    author = StringField("Author", validators=[DataRequired(), Email()])
