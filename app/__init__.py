import os
from dotenv import load_dotenv
load_dotenv()

from flask import Flask, Blueprint
from flaskext.mysql import MySQL
from config import DevelopmentConfig, TestingConfig, ProductionConfig

app = Flask(__name__)

env = os.getenv("FLASK_ENV", "development")

if env == "production":
    app.config.from_object(ProductionConfig)
elif env == "testing":
    app.config.from_object(TestingConfig)
else:
    app.config.from_object(DevelopmentConfig)

mysql = MySQL()
app.config['MYSQL_DATABASE_HOST']='localhost'
app.config['MYSQL_DATABASE_USER']='root'
app.config['MYSQL_DATABASE_PASSWORD']=''
app.config['MYSQL_DATABASE_DB']='lista_regalos'

mysql.init_app(app)

api = Blueprint('api', __name__, url_prefix='/api')

from app.routes import gifts

app.register_blueprint(api)