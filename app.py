from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
import time
import datetime
import pytz
import uuid
import logging
import os

from tests.checkin_test import test_checkin
from utils.get_environment import environment
from routes import routes

"""
WORKON SW

NEED TO NPM RUN BUILD BEFORE BUILDING IMAGEs
db:
fordwh44 pyschedule
psql -U fordwh44 -d pyschedule

docker system prune -a
docker build -t <image_name> .
docker run -p 8000:5000 <image_name>

OR

docker-compose build
docker-compose up -d

heroku container:push web
heroku container:release web
"""
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

flask_app = Flask(__name__,
                static_folder='client/dist/static',
                template_folder='client/dist')

if environment == "dev":
    flask_app.config.from_object("config.DevelopmentConfig")
else:
    flask_app.config.from_object("config.ProductionConfig")

flask_app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(flask_app)
from models import User, Flight

flask_app.register_blueprint(routes)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port)
