from flask import Flask, Blueprint
from ..settings import Config
import inspect


def create_app(config_class):
    flask_app = Flask(__name__)
    flask_app.config.from_object(config_class)
    return flask_app


def register_blueprints(flask_app):
    from app.main import service
    blueprints = inspect.getmembers(service, lambda member: isinstance(member, Blueprint))
    for name, blueprint in blueprints:
        prefix = '/' if name == 'index' else f'/{name.replace("_", "-")}'
        flask_app.register_blueprint(blueprint, url_prefix=prefix)


def register_plugins(flask_app):
    from .plugins import db, ma
    db.init_app(flask_app)
    ma.init_app(flask_app)


def cors_app(flask_app):
    from flask_cors import CORS
    CORS(flask_app)


def populate_initial_data(**kwargs: dict):
    import json
    source = kwargs.pop('data_source')
    from app.main.functions import PopulateDatabaseFunctions, CurrencyConverterApiFunctions
    data = CurrencyConverterApiFunctions.get_exchange_rate_by_date_range(**kwargs)\
        if source == 'API' else json.load(open(Config.MOCK_DATA_JSON, 'r'))

    PopulateDatabaseFunctions.populate(data, source)


def configure_app(config_class):
    flask_app = create_app(config_class)
    register_plugins(flask_app)
    register_blueprints(flask_app)
    cors_app(flask_app)
    return flask_app


flask_app = configure_app(Config)
