from flask import Flask
from flask_server.views import HelloMethodView


class Routes(Flask):
    
    def __init__(self, app):
        self.app = app

    def get_routes(self):
        self.app.add_url_rule('/index', view_func=HelloMethodView.as_view('hello1'))
        return self.app