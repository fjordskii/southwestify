from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import logging
import os

from checkin import auto_checkin


"""
VENV: (pyschedule)
TODO
 -import test checkin method
 -run that
"""


log = logging.getLogger('apscheduler.executors.default')
log.setLevel(logging.INFO)  # DEBUG

fmt = logging.Formatter('%(levelname)s:%(name)s:%(message)s')
h = logging.StreamHandler()
h.setFormatter(fmt)
log.addHandler(h)

flask_app = Flask(__name__)

# initialize scheduler with your preferred timezone
scheduler = BackgroundScheduler({'apscheduler.timezone': 'America/Chicago'})

# add a custom jobstore to persist jobs across sessions (default is in-memory)
# scheduler.add_jobstore('sqlalchemy', url='sqlite:////tmp/schedule.db')
scheduler.start()

####### EXAMPLE CURL CALL
# curl -X POST http://127.0.0.1:5000/schedule-flight  -H 'content-type: application/json' -d '{"time":"2019-12-16T11:17","conf": "ABC123", "fname": "ford", "lname": "beezel"}'
# curl -X POST https://pyschedule.herokuapp.com/schedule-flight  -H 'content-type: application/json' -d '{"time":"2019-12-16T11:17","conf": "ABC123", "fname": "ford", "lname": "beezel"}'
#######

@flask_app.route('/', methods=['GET'])
def hello():
    return 'hello'

@flask_app.route('/schedule-flight', methods=['POST'])
def schedule_to_print():
    data = request.get_json()
    #get time to schedule and text to print from the json
    time = data.get('time')
    conf = data.get('conf')
    fname = data.get('fname')
    lname = data.get('lname')
    #convert to datetime
    date_time = datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
    #schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
    job = scheduler.add_job(auto_checkin, trigger='date', next_run_time=str(date_time),
                            args=[conf, fname, lname])
    return "job details: %s" % job


def printing_something(text):
    print("printing %s at %s" % (text, datetime.now()))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    flask_app.run(threaded=True, port=5000)
