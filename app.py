from flask import Flask, request, render_template, redirect, url_for, jsonify
from flask_cors import CORS
import time
import datetime
import pytz
import uuid
import logging
import os

from tests.checkin_test import test_checkin
from routes import routes

"""
WORKON SW

fordwh44 pyschedule

Check-in attempt 1):
Only ran the last check-in request made, need to figure out multi processing
Need to increase check-in attempts to 40
Need insight into seeing SQL db jobs stored
Need to remove minute buffer and make it something like 5 seconds
Need insight into processes that are sleeping, add naming func?

Got these two responses for some reason:

2019-12-19T23:29:58.886315+00:00 app[web.1]: Sorry! This reservation is not eligible for check in.
2019-12-19T23:30:00.268274+00:00 app[web.1]: Sorry! We can't check you into this flight. Please see a gate agent.
"""
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

flask_app = Flask(__name__)
flask_app.register_blueprint(routes)
CORS(flask_app, resources={r'/*': {'origins': '*'}})

if __name__ == '__main__':
    flask_app.run()
