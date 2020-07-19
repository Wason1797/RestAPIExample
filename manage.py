from app.main.plugins import db
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app.main import populate_initial_data, flask_app
# from app.main.models import CurrencyExchangeRates


flask_app.app_context().push()

manager = Manager(flask_app)

migrate = Migrate(flask_app, db)

manager.add_command('db', MigrateCommand)


@manager.command
def populate(base='EUR', quote='USD', start_date='2020-06-13', end_date='2020-06-18', data_source='API'):
    populate_initial_data(**locals())


@manager.command
def run():
    flask_app.run()


if __name__ == '__main__':
    manager.run()
