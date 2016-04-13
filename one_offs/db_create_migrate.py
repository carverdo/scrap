#!flask/bin/python
"""
We don't really need this module. It's here for these notes (but do note the
procfile)!
Anywhere we see a ref to db_create_migrate.py being entered
in the cmd we could instead enter manager.py (I later replaced that entry below
o get rid of those refs)
=====================
UPGRADES / MIGRATES
=====================
Before running remember to physically create database using postgres!
(Make sure to close all connections / python scripts looking at database
otherwise errors occur.)

Move this script directly beneath app (couldn't fix relative addressing)
RUN this script from the cmd line -

1. Create migrations folder
cd to the folder holding this file.
    C:..> venv\scripts\activate [HAS TO BE BACKSLASH!]
    <venv> C:..> python manager.py db init
(it will say Please edit ... before proceeding; this is not an error, just info.)

2. For EVERY model change (including the first model-overlay on blank dbase)
(each will flash INFO messages)

2a. Generate one empty table: [alembic_version]
     <venv> C:..> python manager.py db migrate

2b. Generate all the other tables
    <venv> C:..> python db_create_migrate.py db upgrade
We can of course also run: > python manager.py db downgrade

3. OPTIONAL (to populate) [can just do via normal python]
    <venv> C:..> python db_init_data.py init_data

============
BACKUPS
============
<venv> C:..> python manager.py alchemydumps create
see https://pypi.python.org/pypi/Flask-AlchemyDumps/0.0.6
"""

from manager import build_manager

if __name__ == '__main__':
    manager = build_manager()
    manager.run()