from flask import render_template
from flask.views import MethodView
from flask_server import appbuilder


class HelloMethodView(MethodView):
    
    def get(self):
        return render_template('index.html', appbuilder=appbuilder)




class ReadMeMethoView(MethodView):

    def get(self):

        return render_template('readme.html',appbuilder=appbuilder)



