import os
from flask_server import CreateApp, db
from flask_migrate import Migrate
from routers import Routes
from flask_appbuilder import AppBuilder


app = CreateApp()

app = app.custom_start_app(os.getenv('FLASK_CONFIG') or 'default')

app = Routes(app)

app = app.get_routes()



#create_dash_application(app)

with app.app_context():
    db.create_all()

migrate = Migrate(app, db)






