import time
import datetime
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


@routes.route('/schedule-flight-form', methods=['POST'])
def schedule_flight():
    data = json.loads(request.data)
    now = datetime.datetime.now()

    conf = data.get('conf')
    fname = data.get('fname')
    lname = data.get('lname')
    user_email = data.get('user_email')

    try:
        auto_checkin(conf, fname, lname, user_email)
        response = jsonify({
            'confirmation': conf,
            'first_name': fname,
            'last_name': lname,
        }), 200
    except Exception as err:
        response = jsonify({
            'error': 'bad request',
            'message': err
        }), 400

    return response


@routes.route('/thanks', methods=['GET'])
def thanks():
    return render_template('thanks.html')
