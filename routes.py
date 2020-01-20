import time
import datetime
import pytz
import uuid
import logging
import os

from flask import Blueprint, render_template
from flask import request, render_template, url_for, jsonify

from scheduler import scheduler
from checkin import auto_checkin

routes = Blueprint('routes', __name__)

# sanity check route
@routes.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@routes.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@routes.route('/schedule-flight-form', methods=['POST'])
def schedule_flight():
    data = request.form
    now = datetime.datetime.now()
    unique_id = uuid.uuid4().hex
    now_plus_1 = now + datetime.timedelta(minutes = 1)
    now_plus_1 = now_plus_1.replace(second=0, microsecond=0)

    conf = data.get('conf')
    fname = data.get('fname')
    lname = data.get('lname')

    print('Check in details: {} {} {}. Running at {}'.format(conf, fname, lname, now_plus_1))

    # job = scheduler.add_job(test_checkin, trigger='date', next_run_time=str(now_plus_1))
    job = scheduler.add_job(auto_checkin, trigger='date', next_run_time=str(now_plus_1),
                            args=[conf, fname, lname], id=unique_id, replace_existing=True)
    return render_template('thanks.html', data={
        'confirmation': conf,
        'first_name': fname,
        'last_name': lname,
        'scheduled_for': now_plus_1
    })


@routes.route('/thanks', methods=['GET'])
def thanks():
    return render_template('thanks.html')
