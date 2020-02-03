from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
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

fordwh44 pyschedule
docker build -t flaskdockkk .
docker run -p 8000:5000 flaskdockkk
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

flask_app.register_blueprint(routes)

if __name__ == '__main__':
    # Bind to PORT if defined, otherwise default to 5000.
    port = int(os.environ.get('PORT', 5000))
    flask_app.run(host='0.0.0.0', port=port)
