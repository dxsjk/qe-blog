from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
from flask_login import LoginManager
from flask_migrate import Migrate
import os
MYSQL_HOST = os.getenv('MYSQL_HOST', 'localhost')
MYSQL_USER = os.getenv('MYSQL_USER', 'root')
MYSQL_PASSWORD = os.getenv('MYSQL_PASSWORD', '123456')
MYSQL_DB = os.getenv('MYSQL_DB', 'flaskdb')
MYSQL_PORT = os.getenv('MYSQL_PORT', '3306')

app = Flask(__name__,
            template_folder='../dist',
            static_folder='../dist/static'
            )
app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+mysqldb://{MYSQL_USER}:{MYSQL_PASSWORD}@{MYSQL_HOST}:{MYSQL_PORT}/{MYSQL_DB}'
app.config['SECRET_KEY'] = '123456'

db = SQLAlchemy(app)
ma = Marshmallow(app)
login_manager = LoginManager(app)
migrate = Migrate(app, db)
from routes import article_routes, user_routes, image_routes,admin_routes,cal_routes
from models import users, article
with app.app_context():
    db.create_all()
