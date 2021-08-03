from flask import Flask
from config import Config
from .site.routes import site
from .authentication.routes import auth
from flask_migrate import Migrate
from .models import db

app = Flask(__name__)

app.config.from_object(Config)

app.register_blueprint(site) #register the blueprint class known as 'site'
app.register_blueprint(auth) #register the blueprint class known as 'auth'

db.init_app(app) #database init gives the db access to the entire app set in line 8

migrate = Migrate(app, db)

from .models import User