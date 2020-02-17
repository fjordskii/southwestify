from datetime import datetime
from datetime import timedelta
from math import trunc
from docopt import docopt
from pytz import utc
from southwest import Reservation, openflights
from threading import Thread
import sys
import time
import uuid

from scheduler import scheduler
from utils.email_utils import send_email

CHECKIN_EARLY_SECONDS = 5

def final_checkin(reservation):
    data = reservation.checkin()
    for flight in data['flights']:
        for doc in flight['passengers']:
            message = "{} got {}{}!".format(doc['name'], doc['boardingGroup'], doc['boardingPosition'])
            print(message)
            send_email(data=doc, email='thecuatro@gmail.com')

def schedule_checkin(flight_time, reservation):
    unique_id = uuid.uuid4().hex
    checkin_time = flight_time - timedelta(days=1)
    current_time = datetime.utcnow().replace(tzinfo=utc)
    # check to see if we need to sleep until 24 hours before fligh
    if checkin_time > current_time:
        # calculate duration to sleep
        delta = (checkin_time - current_time).total_seconds() - CHECKIN_EARLY_SECONDS
        job_time = checkin_time - timedelta(seconds=CHECKIN_EARLY_SECONDS)
        # pretty print our wait time
        m, s = divmod(delta, 60)
        h, m = divmod(m, 60)
        message = "Too early to check in.  Waiting {} hours, {} minutes, {} seconds".format(trunc(h), trunc(m), s)
        print(message)
        send_email(data=None, email='thecuatro@gmail.com', msg=message)
        try:
            job = scheduler.add_job(final_checkin, trigger='date', next_run_time=str(job_time),
                args=[reservation], id=reservation.number, replace_existing=True)
            print('Scheduled check in to run in {}'.format(delta))
        except OverflowError:
            print("System unable to sleep for that long, try checking in closer to your departure date")
            sys.exit(1)
    # data = reservation.checkin()
    # for flight in data['flights']:
    #     for doc in flight['passengers']:
    #         message = "{} got {}{}!".format(doc['name'], doc['boardingGroup'], doc['boardingPosition'])
    #         print(message)
    #         send_email(data=doc, email='thecuatro@gmail.com')

def auto_checkin(reservation_number, first_name, last_name, verbose=False):
    try:
        scheduled_job = scheduler.get_job(reservation_number)
    except:
        scheduled_job = None

    if not scheduled_job:
        r = Reservation(reservation_number, first_name, last_name, verbose)
        body = r.lookup_existing_reservation()

        if body:
            # Get our local current time
            now = datetime.utcnow().replace(tzinfo=utc)
            tomorrow = now + timedelta(days=1)

            for leg in body['bounds']:
                # calculate departure for this leg
                airport = "{}, {}".format(leg['departureAirport']['name'], leg['departureAirport']['state'])
                takeoff = "{} {}".format(leg['departureDate'], leg['departureTime'])
                airport_tz = openflights.timezone_for_airport(leg['departureAirport']['code'])
                date = airport_tz.localize(datetime.strptime(takeoff, '%Y-%m-%d %H:%M'))
                if date > now:
                  schedule_checkin(date, r)
        else:
            raise 'Bad request made, body is empty.'
    else:
        print('already checked you in fam')
