import smtplib


def _generate_subject(data={}):
    return 'Congrats! You are checked-in! {}{}'.format(data['boardingGroup'], data['boardingPosition'])


def _generate_text(data={}):
    return 'Congratulations! You have successfully checked-in to your SouthWest flight: Passenger {} got position {}{}.'.format(data['name'], data['boardingGroup'], data['boardingPosition'])


def send_email(data, msg=None):
    s = smtplib.SMTP('smtp.gmail.com', 587)
    s.starttls()
    s.login("firebreathrecords", "Fwhiv$123!")

    if msg:
        SUBJECT = 'Scheduled Check-in!'
        TEXT = msg
    else :
        SUBJECT = _generate_subject(data)
        TEXT = _generate_text(data)
    message = 'Subject: {}\n\n{}'.format(SUBJECT, TEXT)
    s.sendmail("you@gmail.com", "fordheacock@gmail.com", message)

    s.quit()

# doc['name'], doc['boardingGroup'], doc['boardingPosition']
