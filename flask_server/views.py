from flask.views import MethodView


class HelloMethodView(MethodView):

    def get(self):
        return 'Hola'