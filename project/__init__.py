import os
from flask import Flask
from flask_mail import Mail


mail = Mail()
flask_app = Flask(__name__)

flask_app.config.from_object('config.DevelopmentConfig')
mail.init_app(flask_app)


