from flask import Flask
from flask_appbuilder import AppBuilder
from flask_sqlalchemy import SQLAlchemy
from flask_caching import Cache
from flask_bootstrap import Bootstrap
from config import config
from dash import Dash
import dash_bootstrap_components as dbc
import logging
import os

db = SQLAlchemy()
cache = Cache()
bootstrap = Bootstrap()
appbuilder = AppBuilder()

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)


class CreateApp():

    def __init__(self):
        self.app = Flask(__name__)

    def custom_start_app(self, config_name):
        app = self.app
        app.config.from_object(config[config_name])
        db.init_app(app)
        cache.init_app(app)
        bootstrap.init_app(app)
        
        from dash_application.callbacks import register_callback as dash_callback
        from dash_application.layout import layout as dash_layout
        register_dash_app(
            flask_server=app,
            title='EANT-DA-PROYECTO-FINAL',
            base_pathname='/dash/',
            layout=dash_layout,
            register_callbacks_funcs=[dash_callback]
        )

        with app.app_context():
            appbuilder.init_app(app, db.session)


        return app



def register_dash_app(flask_server, title, base_pathname, layout, register_callbacks_funcs):
    # Meta tags for viewport responsiveness
    meta_viewport = {"name": "viewport", "content": "width=device-width, initial-scale=1, shrink-to-fit=no"}

    my_dash_app = Dash(
        __name__,
        server=flask_server,
        url_base_pathname=base_pathname,
        assets_folder=  os.path.join(os.path.abspath('..'), 'dash_application','assets'),
        meta_tags=[meta_viewport],
        external_stylesheets=[dbc.themes.FLATLY, '\assets\style.css'],
        
    )
    
    with flask_server.app_context():
        my_dash_app.title = title
        my_dash_app.layout = layout
        my_dash_app._favicon =  os.path.join(os.path.abspath(os.path.dirname(__file__)).split('flask_server')[0], 'dash_application','assets', 'favicon.ico')
        for call_back_func in register_callbacks_funcs:
            call_back_func(my_dash_app)




