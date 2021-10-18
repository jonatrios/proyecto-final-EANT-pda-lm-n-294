import os
from dotenv import load_dotenv
from flask import url_for

basedir = os.path.abspath(os.path.dirname(__file__))

load_dotenv(basedir + '\.env')

class Config():
    SECRET_KEY = os.environ.get('SECRET_KEY')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    CACHE_TYPE = "SimpleCache"
    CACHE_DEFAULT_TIMEOUT = 300
    APP_THEME = "flatly.css"
    APP_NAME = "EANT-DA-PROYECTO-FINAL"
    #APP_ICON = '/dash_application/assets/favicon.ico'

    


    @staticmethod
    def init_app(self):
        pass


class DevelopmentConfig(Config):
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = os.environ.get('DEV_DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data-dev.sqlite')



class ProductionConfig(Config):
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'data.sqlite')


config = {
'development': DevelopmentConfig,
'production': ProductionConfig,
'default': DevelopmentConfig
}