import time
import datetime
import uuid
import os
import json

from flask import request, render_template, url_for, jsonify, Blueprint, redirect

from scheduler import scheduler
from checkin import auto_checkin
from utils.get_environment import environment

routes = Blueprint('routes', __name__)

@routes.context_processor
def inject_stage_and_region():
    return dict(environment=environment)

@routes.route('/', defaults={'path': ''})
@routes.route('/<path:path>')
def index(path):
    return render_template('index.html')

@routes.route('/ping', methods=['GET'])
def ping_pong():
    return jsonify('pong!')

@routes.route('/schedule-flight-form', methods=['POST'])
def schedule_flight():
    data = json.loads(request.data)
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
    return jsonify({
        'confirmation': conf,
        'first_name': fname,
        'last_name': lname,
        'scheduled_for': now_plus_1
    })

@routes.route('/thanks', methods=['GET'])
def thanks():
    return render_template('thanks.html')

@routes.route('/register', methods=['POST'])
def register():
    from firebase import auth

    data = json.loads(request.data)
    email = data.get('email')
    password = data.get('password')

    user = auth.create_user_with_email_and_password(email, password)
    data = jsonify({ 'user_id': user['idToken'], 'email': user['email'] })
    return data

@routes.route('/login', methods=['POST'])
def login():
    from firebase import auth

    data = json.loads(request.data)
    email = data.get('email')
    password = data.get('password')

    user = auth.sign_in_with_email_and_password(email, password)
    data = jsonify({ 'user_id': user['idToken'], 'email': user['email'] })
    return data
