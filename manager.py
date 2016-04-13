"""
This is a neat way of adding commands that we can use in the cmd module.
We haven't, but perhaps could have created manager as part of the the app init.
Now we add objects so we can access via cmd line;
e.g. app, db, Member etc.

Get rid of manager.run() and you can play around in the gui.

TO USE IN CMD:
1. As ever, activate your venv (venv\scripts\activate).
2. Then <venv> > python manager.py shell [OR whatever other command suits]
"""
__author__ = 'donal'
__project__ = 'dcleaner'

from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand
from flask_alchemydumps import AlchemyDumps, AlchemyDumpsCommand
from run import app
from app import db
from app.db_models import Member


# =================
# BUILD MANAGER (for cmd handling)
# =================
def build_manager():
    manager = Manager(app)
    # ADD DB COMMAND
    manager.add_command('db', MigrateCommand)
    migrate = Migrate(app, db)

    # ADD SHELL COMMANDS
    def _make_context():
        return dict(app=app, db=db, Member=Member, use_ipython=False)
    manager.add_command('shell', Shell(make_context=_make_context))

    # TEST
    @manager.command
    def hello():
        print "hello"

    # init Alchemy Dumps (local db table backups)
    alchemydumps = AlchemyDumps(app, db)
    manager.add_command('alchemydumps', AlchemyDumpsCommand)
    return manager


# IMPORTANT! (run updates manager, locks the commands in)
if __name__ == '__main__':
    manager = build_manager()
    manager.run()
