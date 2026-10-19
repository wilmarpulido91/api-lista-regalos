import os

from flask import Flask, Blueprint
from flask_cors import CORS
from flaskext.mysql import MySQL
from config import DevelopmentConfig, TestingConfig, ProductionConfig

app = Flask(__name__)
CORS(app)

env = os.getenv("FLASK_ENV", "development")

if env == "production":
    app.config.from_object(ProductionConfig)
elif env == "testing":
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST'] = os.environ.get('DB_HOST')
app.config['MYSQL_DATABASE_PORT'] = int(os.environ.get('DB_PORT', 3306))
app.config['MYSQL_DATABASE_USER'] = os.environ.get('DB_USER')
app.config['MYSQL_DATABASE_PASSWORD'] = os.environ.get('DB_PASSWORD')
app.config['MYSQL_DATABASE_DB'] = os.environ.get('DB_NAME')

mysql.init_app(app)

api = Blueprint('api', __name__, url_prefix='/api')

from app.routes import gifts, guests, register

app.register_blueprint(api)