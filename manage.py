# All the database migration commands can be accessed by running this script:
    # python manage.py db init      Create a migration repository (only need to run once)
    # python manage.py db migrate   Generate an initial migration
    # python manage.py db upgrade   Confirm desired changes are detected (else edit migration script), and apply migration to db:

# (Each time the database models change repeat the migrate and upgrade commands.)

import os
from flask_script import Manager
# Flask-Migrate is a package that extends Flask to use sqla db migrations using alembic
# The MigrateCommand class is only used when it is desired to expose database
# migration commands through the Flask-Script extension
from flask_migrate import Migrate, MigrateCommand

from app import app, db

app.config.from_object(os.environ['APP_SETTINGS'])

# Initialize the Flask-Migrate extension with the standard Flask command-line interface
# Pass application instance (app) and the Flask-SQLAlchemy database instance (db) as args to
# Flask-Migrate's Migrate class
migrate = Migrate(app, db)

# Instantiate Manage class to manage scripts
manager = Manager(app)

# Call add_command on manager instance to add a command to flask-script.
# Run MigrateCommand when user types 'db' in command line
manager.add_command('db', MigrateCommand)


if __name__ == '__main__':
    manager.run()
