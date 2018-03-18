# sql.py - Create a SQLite3 DB with tables and dummy data

import sqlite3

with sqlite3.connect("pierce.db") as connection:

    # Get cursor object for interacting with database
    c = connection.cursor()

    # Create posts table
    c.execute("""CREATE TABLE IF NOT EXISTS posts
              (post_id INTEGER PRIMARY KEY, title TEXT, video TEXT, post TEXT)
              """)

    # Dummy post data
    posts = [
        {
            "title": "Hello World!",
            "video": "https://www.facebook.com/plugins/video.php?href=https%3A%2F%2Fwww.facebook.com%2Fmathew.s.pierce.5%2Fvideos%2F10214268153165023%2F&show_text=0&width=560",
            "post": "This is a test of database stuff"
        },
        {
            "title": "Second Post!",
            "video": "https://www.youtube.com/embed/UO3h4FBLWqY",
            "post": "This is a test of more database stuff"
        }
    ]

    # Insert dummy data into the posts table
    for post in posts:
        query = 'INSERT INTO posts VALUES("{title}", "{video}", "{post}")'
        c.execute(query.format(**post))
