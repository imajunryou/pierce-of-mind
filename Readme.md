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
  + Point the environment variable "PIERCE\_OF\_MIND\_CONFIG" to this file.
+ Setup your local database
  + If you already have a local copy of the database, skip this section
  + Run the sql.py script (sister to config.py) from the same folder as manage.py

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
A short script is included that will build a basic SQLite3 database, with tables and initial content.  This should be run only once, and only for the purpose of testing.  It will clobber any actual database and its content, and is provided exclusively to get you up off the ground.

To run the script, navigate to whichever folder contains `manage.py`, and then call the following:

```bash
python3 pierce_of_mind/sql.py
```

This will build a small database titled `pierce.db`, adjacent to `manage.py`.  This database will be used for persisting any content that exists for the site.

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
