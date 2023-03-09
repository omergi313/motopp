from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager
import logging
import os

db = SQLAlchemy()
logging.basicConfig(filename='app.log', level=logging.INFO, format='%(asctime)s %(levelname)s: %(message)s')

user = "root"
if 'ogindes' in os.environ.get("PWD"):
    host = "localhost"
    password = "idkbro"
    logging.info('$'*50)
    logging.info('ogindes')
    logging.info('$' * 50)
else:
    logging.info('$'*50)
    logging.info('baaaaaaaa')
    host = "mysql"
    password = ""
    logging.info('$' * 50)



def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = '1234567890'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'mysql+pymysql://{user}:{password}@{host}:3306/motopp'
    app.config['SQLALCHEMY_ECHO'] = True

    db.init_app(app)
    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .models import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    with app.app_context():
        db.create_all()

    return app
