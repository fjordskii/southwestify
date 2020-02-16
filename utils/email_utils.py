import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

def _generate_subject(data={}):
    return 'Congrats! You are checked-in! {}{}'.format(data['boardingGroup'], data['boardingPosition'])

def _generate_text(data={}):
    return 'Congratulations! You have successfully checked-in to your SouthWest flight: Passenger {} got position {}{}.'.format(data['name'], data['boardingGroup'], data['boardingPosition'])

def send_email(data, email, msg=None):
    if msg:
        SUBJECT = 'Scheduled Check-in! CheckIntoMyFlight.com '
        TEXT = msg
    else :
        SUBJECT = _generate_subject(data)
        TEXT = _generate_text(data)
    message = Mail(
        from_email='donotreploy@checkintomyflight.com',
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


