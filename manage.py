from flask.ext.script import Manager
from flask.ext.migrate import Migrate, MigrateCommand
from airtng_flask import app, db

migrate = Migrate(app, db)

manager = Manager(app)
manager.add_command('db', MigrateCommand)

@manager.command
def test():
    import sys, unittest
    tests = unittest.TestLoader().discover('.', pattern="*_testing.py")
    result = unittest.TextTestRunner(verbosity=1).run(tests)

    if not result.wasSuccessful():
            sys.exit(1)


if __name__ == "__main__":
    manager.run()
