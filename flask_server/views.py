from flask import render_template
from flask.views import MethodView
from flask_appbuilder.views import BaseView
from flask_appbuilder import expose
from flask_server import appbuilder

class HelloMethodView(MethodView):

    def get(self):
        return render_template('index.html', appbuilder=appbuilder)



class FirstBaseView(BaseView):
    route_base = 'index/'

    @expose('/hello/')
    def hello(self):
        return 'Hello'

appbuilder.add_view_no_menu(FirstBaseView())





