# manage.py

from pierce_of_mind import app as pierce_app
from pierce_of_mind import db
from pierce_of_mind.main.models import Post

from flask_script import Manager, prompt_bool

# Either the config level is set in an environment variable
# or we just use the development version of the config
app = pierce_app

manager = Manager(app)


@manager.command
def initdb():
    db.create_all()
    print("Initialized the database.")


@manager.command
def dropdb():
    if prompt_bool("Are you sure you want to lose all of your data?"):
        db.drop_all()
        print("Database dropped!")


@manager.command
def populatedb():
    if prompt_bool("Are you sure you want to inject fake data?"):
        p = [
            Post(
                title="First Post!",
                content="  ".join(
                    (
                        "This is the first post inserted into the database.",
                        "Ever so exciting!"
                    )
                ),
                author="cshepard@bruinmail.slcc.edu",
            ), Post(
                title="Second Post!",
                content="  ".join(
                    (
                        "This is the second post.",
                        "It has three lines of text.",
                        "Because I feel fancy."
                    )
                ),
                author="cshepard@bruinmail.slcc.edu",
            ), Post(
                title="Adventures Among the Roses",
                content="  ".join(
                    (
                        "This video is about some random thing that was easy to find a url for.",
                        "Enjoy!"
                     )
                ),
                video="https://www.youtube-nocookie.com/embed/-6Wu0Q7x5D0?rel=0",
                author="cshepard@bruinmail.slcc.edu",
            )
        ]
        for post in p:
            db.session.add(post)
        db.session.commit()


if __name__ == "__main__":
    manager.run()
