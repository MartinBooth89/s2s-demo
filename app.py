from flask import Flask, g
from flask_smorest import Api
from db import db
from resources import ProductBlueprint

app = Flask(__name__)

# API configuration
app.config["API_TITLE"] = "Stores REST API"
app.config["API_VERSION"] = "v1"
app.config["OPENAPI_VERSION"] = "3.0.3"
app.config["OPENAPI_URL_PREFIX"] = "/"
app.config["OPENAPI_SWAGGER_UI_PATH"] = "/swagger-ui"
app.config[
    "OPENAPI_SWAGGER_UI_URL"
] = "https://cdn.jsdelivr.net/npm/swagger-ui-dist/"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///datastore.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["PROPAGATE_EXCEPTIONS"] = True

# initialise database
db.init_app(app)
api = Api(app)

# create database for first time use
with app.app_context():
    db.create_all()

api.register_blueprint(ProductBlueprint)
# add blueprints for additional resources here