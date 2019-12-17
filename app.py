from flask import Flask, request, render_template, redirect, url_for
from apscheduler.schedulers.background import BackgroundScheduler
from apscheduler.schedulers.asyncio import AsyncIOScheduler
from apscheduler.schedulers.blocking import BlockingScheduler
from apscheduler.jobstores.sqlalchemy import SQLAlchemyJobStore
import asyncio
import time
import datetime
import pytz
import logging
import os

from checkin import auto_checkin


"""
VENV: (pyschedule)
TODO
 -import test checkin method
 -run that
 -conf example: NFMIU4/NFO8SY
 -(it works without apscheduler)

"""

############ LOGGING ############
log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)
############ LOGGING ############

flask_app = Flask(__name__)

# initialize scheduler with preferred timezone. Implements jobstore for persistance
scheduler = BackgroundScheduler({'apscheduler.timezone': 'America/Chicago'}, jobstores={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})

scheduler.start()

@flask_app.route('/', methods=['GET'])
def hello():
    return render_template('index.html')


@flask_app.route('/schedule-flight', methods=['POST'])
def schedule_flight_direct():
    # bypasses form POST if wanted, can hit with curl for example:
    # curl -X POST https://pyschedule.herokuapp.com/schedule-flight  -H 'content-type: application/json' -d '{"time":"2019-12-17T12:42", "conf": "ABC123", "fname": "Bob", "lname": "Saget"}
    data = request.get_json()

    time = data.get('time')
    conf = data.get('conf')
    fname = data.get('fname')
    lname = data.get('lname')
    # convert to datetime
    date_time = datetime.datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
    # schedule job
    job = scheduler.add_job(auto_checkin, trigger='date', next_run_time=str(date_time),
                            args=[conf, fname, lname], jobstore={'default': SQLAlchemyJobStore(url='sqlite:///jobs.sqlite')})
    return "job details: %s" % job


@flask_app.route('/schedule-flight-form', methods=['POST'])
def schedule_flight():
    data = request.form
    # get current time and add one minute to delay scheduled job
    now = datetime.datetime.now()
    now_plus_1 = now + datetime.timedelta(minutes = 1)
    now_plus_1 = now_plus_1.replace(second=0, microsecond=0)

    conf = data.get('conf')
    fname = data.get('fname')
    lname = data.get('lname')

    print('Check in details: {} {} {}. Running at {}'.format(conf, fname, lname, now_plus_1))
    job = scheduler.add_job(auto_checkin, trigger='date', next_run_time=str(now_plus_1),
                            args=[conf, fname, lname])
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
