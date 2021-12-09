from flask import Flask
from flaskext.mysql import MySQL
from catalog.mysql_env import *
import os

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'js'}

app = Flask(__name__)

# setting mysql
mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = db_user
app.config['MYSQL_DATABASE_PASSWORD'] = db_password
app.config['MYSQL_DATABASE_DB'] = db_name
app.config['MYSQL_DATABASE_HOST'] = db_host
mysql.init_app(app)
conn = mysql.connect()

app.config['SECRET_KEY'] = 'ec9439cfc6c796ae2029594d'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config["MAX_IMAGE_FILESIZE"] = 0.5 * 1024 * 1024

from catalog import routes
