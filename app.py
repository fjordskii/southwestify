from flask import Flask, request
from apscheduler.schedulers.background import BackgroundScheduler
from datetime import datetime
import logging
import os


"""
TODO
 -Figure out requirements.txt on pythonanywhere
 -check you can POST to PA remote route
 -check logs to make sure it prints
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
# curl -X POST http://127.0.0.1:5000/schedulePrint  -H 'content-type: application/json' -d '{"time":"2018-07-27T01:25","text": "apscheduler"}'
# curl -X POST http://fordwh44.pythonanywhere.com/schedulePrint  -H 'content-type: application/json' -d '{"time":"2019-12-16T10:10","text": "apscheduler"}'
#######

@flask_app.route('/', methods=['GET'])
def hello():
    return 'hello'

@flask_app.route('/schedulePrint', methods=['POST'])
def schedule_to_print():
    data = request.get_json()
    #get time to schedule and text to print from the json
    time = data.get('time')
    text = data.get('text')
    #convert to datetime
    date_time = datetime.strptime(str(time), '%Y-%m-%dT%H:%M')
    #schedule the method 'printing_something' to run the the given 'date_time' with the args 'text'
    job = scheduler.add_job(printing_something, trigger='date', next_run_time=str(date_time),
                            args=[text])
    return "job details: %s" % job


def printing_something(text):
    print("printing %s at %s" % (text, datetime.now()))


if __name__ == '__main__':
    # Threaded option to enable multiple instances for multiple user access support
    flask_app.run(threaded=True, port=5000)
