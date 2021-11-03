import json
from flask import render_template, Response, request
from flask.views import MethodView
from flask_server import appbuilder
from .utils import get_info, get_resources, cache_data

class HelloMethodView(MethodView):
    
    def get(self):
        return render_template('index.html', appbuilder=appbuilder)




class ReadMeMethoView(MethodView):

    def get(self):

        return render_template('readme.html',appbuilder=appbuilder)


class ApiMethodView(MethodView):

    def get(self):
        group = request.args.get('group') if request.args.get('group') != None else ''
        organization = request.args.get('organization') if request.args.get('organization') != None else ''
        tags = request.args.get('tags') if request.args.get('tags') != None else ''
        page = request.args.get('page') if request.args.get('page') != None else 1
        prefix = request.args.get('prefix')
        resource = request.args.get('resource')
        if resource:
            return Response(json.dumps(cache_data(resource=resource), indent=3, ensure_ascii=False), content_type='application/json')
        if prefix:
            return Response(json.dumps(get_resources(prefix=prefix), indent=3, ensure_ascii=False), content_type='application/json') 
        return Response(json.dumps(get_info(group=group,organization=organization,tags=tags, page=page), indent=3, ensure_ascii=False), content_type='application/json')