from app.main.plugins import db
from flask_script import Manager
from app.main import populate_initial_data, flask_app
from flask_migrate import Migrate, MigrateCommand


flask_app.app_context().push()

manager = Manager(flask_app)

migrate = Migrate(flask_app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def populate(source='API'):
    populate_initial_data(source)


@manager.command
def run():
    flask_app.run()


if __name__ == '__main__':
    manager.run()
