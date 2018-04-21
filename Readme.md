# Pierce of Mind
Pierce of Mind is a [podcast](https://itunes.apple.com/us/podcast/pierce-of-mind-podcast/id1141487509?mt=2) by Matthew Pierce.  This project is a blog for the podcast.

# Setup
To get up and running, there are 3 broad steps that you need to accomplish:

+ Clone the repository - This can be done through Github.
+ Install the requirements (see Requirements.txt for the most up-to-date list)
  + Python 3
  + Flask
  + Flask-Script
+ Configure your local copy
  + Create a file called "settings.cfg" in the same folder as the file `config.py`.
  + Configure your secret key (see below)
  + Point the environment variable "PIERCE\_OF\_MIND\_CONFIG" to this file.
+ Setup your local database
  + If you already have a local copy of the database, skip this section
  + Run the sql.py script (sister to config.py) from the same folder as manage.py

## Configuring the Secret Key
You need a secret key inside your settings.cfg file in order for various parts of the site (such as authentication and post editing) to work.  The line should be like so:

```python
SECRET_KEY='your_secret_key_here'
```

The capitalization, and spelling, of `SECRET_KEY` are important.  The equal sign, and the lack of spaces around it are also important.  The single quotes around the secret key are important, too.

What should your secret key be?  Something hard to guess.  Since you won't be manually typing it in, it is probably best to have it be something really annoying.  Here is a bit of Python that will spit out random unicode strings that could be used:

```python
>>> import os
>>> os.urandom(24)
b'\xfd{H\xe5<\x95\xf9\xe3\x96.5\xd1\x01O<!\xd5\xa2\xa0\x9fR"\xa1\xa8'
```

Copy-paste everything in the quotes (ignoring the starting b outside the quotes), and use that as your secret key.  **DO NOT** use the key that is actually written above.  It isn't secret.

## Configuring Environment variables
On Linux or MacOS, this can be done with:

```bash
export PIERCE_OF_MIND_CONFIG=path/to/settings.cfg
```

On Windows, this can be done with:

```
set PIERCE_OF_MIND_CONFIG=path\to\settings.cfg
```

## Initially Building the Database
Several commands are included within the `manage.py` script which can be used to configure the database.  It will clobber any actual database and its content, and is provided exclusively to get you up off the ground.

The available commands are as follows:

```bash
python3 manage.py dropdb
```

This will drop the current database, and **destroy all data** that the database contains.  **THIS IS NOT REVERSABLE** unless you have a backup of your database somewhere.  **YOUR DATABASE IS NOT BACKED UP TO THE REPOSITORY**, so you have to manually back it up!

```bash
python3 manage.py initdb
```

This will build a small database titled `pierceofmind.db`, located adjacent to `manage.py`.  This database is used to persist any content that exists for the site.

This will also create new tables in the database, using the latest structure information available.  This should be run when first building the database, or immediately after dropping the database with the previous command.  It won't work well if run on an existing database with content.

```bash
python3 manage.py populatedb
```

This will inject some fake data into the database.  Why would you want that?  For testing, mostly.  Once you are in a position to put actual data into the system, you shouldn't use this command.

# Starting a local server
Navigate to your local copy of this repository, and enter the following:

```bash
python manage.py runserver
```

If you have multiple copies of Python, you may need to specify which version you want to use:

```bash
python3 manage.py runserver
```

If you successfully activate the server, you should see something like:

```bash
 * Running on http://127.0.0.1:5000/ (Press CTRL+C to quit)
 * Restarting with stat
 * Debugger is active!
 * Debugger PIN: 334-652-202
```

Navigating to the given URL, `http://127.0.0.1:5000/` in the above example, and you should see your local copy of the site up and running.
