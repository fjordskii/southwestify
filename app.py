from flask import Flask, request, render_template, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
from apscheduler.executors.pool import ThreadPoolExecutor, ProcessPoolExecutor
import time
import datetime
import pytz
import uuid
import logging
import os

from checkin import auto_checkin
from tests.checkin_test import test_checkin

"""
WORKON SW

fordsw swdatabase

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

scheduler = BackgroundScheduler({
    'apscheduler.jobstores.default': {
        'type': 'sqlalchemy',
        'url': 'sqlite:///jobs.sqlite'
    },
    'apscheduler.executors.default': {
        'class': 'apscheduler.executors.pool:ThreadPoolExecutor',
        'max_workers': '20'
    },
    'apscheduler.executors.processpool': {
        'type': 'processpool',
        'max_workers': '5'
    },
    'apscheduler.job_defaults.coalesce': 'false',
    'apscheduler.job_defaults.max_instances': '3',
    'apscheduler.timezone': 'America/Chicago',
})

scheduler.start()

############# ROUTES #############
@flask_app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@flask_app.route('/schedule-flight-form', methods=['POST'])
def schedule_flight():
    data = request.form
    now = datetime.datetime.now()
    unique_id = uuid.uuid4()
    now_plus_1 = now + datetime.timedelta(minutes = 1)
    now_plus_1 = now_plus_1.replace(second=0, microsecond=0)

    conf = data.get('conf')
    fname = data.get('fname')
    lname = data.get('lname')

    print('Check in details: {} {} {}. Running at {}'.format(conf, fname, lname, now_plus_1))

    # job = scheduler.add_job(test_checkin, trigger='date', next_run_time=str(now_plus_1))
    job = scheduler.add_job(auto_checkin, trigger='date', next_run_time=str(now_plus_1),
                            args=[conf, fname, lname], id=str(unique_id), replace_existing=True)
    return render_template('thanks.html', data={
        'confirmation': conf,
        'first_name': fname,
        'last_name': lname,
        'scheduled_for': now_plus_1
    })


@flask_app.route('/thanks', methods=['GET'])
def thanks():
    return render_template('thanks.html')


if __name__ == '__main__':
    flask_app.run()
