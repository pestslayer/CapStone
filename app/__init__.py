from flask import Flask
from config import Config
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db as root_db, ma
from .api.routes import api
from flask_cors import CORS
from helpers import JSONEncoder

app = Flask(__name__)
CORS(app)

app.register_blueprint(api)

app.json_encoder = JSONEncoder
app.config.from_object(Config)
root_db.init_app(app)
ma.init_app(app)
migrate = Migrate(app, root_db)