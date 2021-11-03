from flask import Flask
from flask_server.views import HelloMethodView, ReadMeMethoView, ApiMethodView


class Routes(Flask):
    
    def __init__(self, app):
        self.app = app

    def get_routes(self):
        self.app.add_url_rule('/', view_func=HelloMethodView.as_view('hello1'))
        self.app.add_url_rule('/readme', view_func=ReadMeMethoView.as_view('read_me'))
        self.app.add_url_rule('/api/v1/datasets', view_func=ApiMethodView.as_view('api'))
        return self.app