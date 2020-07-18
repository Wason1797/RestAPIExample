import os


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


class Config:
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = 'sqlite:///{}'.format(os.path.join(BASE_DIR, 'db.sqlite'))
    INITIAL_START_DATE = '2020-07-13'
    INITIAL_END_DATE = '2020-07-18'
    INITIAL_BASE = 'EUR'
    INITIAL_QUOTE = 'USD'
    MOCK_DATA_JSON = ''
