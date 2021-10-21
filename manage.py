import os
from flask_server import CreateApp, db
from flask_migrate import Migrate
from routers import Routes



app = CreateApp()

app = app.custom_start_app(os.getenv('FLASK_CONFIG') or 'default')

app = Routes(app)

app = app.get_routes()




with app.app_context():
    db.create_all()

migrate = Migrate(app, db)


if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(port=port)



