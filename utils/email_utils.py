import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail


def _generate_subject(data={}):
    return 'Congrats! You are checked-in! {}{} - AutomateMyCheckin.com'.format(data['boardingGroup'], data['boardingPosition'])


def _generate_text(data={}):
    return 'Congratulations! You have successfully checked-in to your SouthWest flight: Passenger {} got position {}{}. Thanks for using AutomateMyCheckin.com'.format(data['name'], data['boardingGroup'], data['boardingPosition'])


def send_email(data, email):
    if data.get('reservation', None):
        reservation = data.get('reservation')
        FULL_NAME = '{} {}'.format(reservation.first, reservation.last)
        SUBJECT = 'Scheduled Check-in! AutomateMyCheckin.com'
        TEXT = 'Congrats! We have successfully scheduled a flight check-in for {} with the reservation number {} on {}. We will email you again when the check-in runs to let you know what seat you got! Thanks for using automatemycheckin.com'.format(
            FULL_NAME, reservation.number, data.get('checkin_time'))
    else:
        SUBJECT = _generate_subject(data)
        TEXT = _generate_text(data)
    message = Mail(
        from_email='donotreply@automatemycheckin.com',
        to_emails=email,
        subject=SUBJECT,
        html_content=TEXT)
    try:
        sg = SendGridAPIClient(os.environ.get('SENDGRID_API_KEY'))
        response = sg.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e.message)
