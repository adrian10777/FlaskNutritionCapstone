from flask import Flask
from config import Config
from flask_cors import CORS

from .api.routes2 import api
from .payments.routesstripe import payments
# import blueprints
from flask_sqlalchemy import SQLAlchemy

from .models import db
from flask_migrate import Migrate

app = Flask(__name__)
CORS(app, origins=['*'])

app.config.from_object(Config)

app.register_blueprint(api)
app.register_blueprint(payments)

db.init_app(app)
migrate = Migrate(app, db)
from . import routes

