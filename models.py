from app import db

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    confirmation_number = db.Column(db.String())
    first_name = db.Column(db.String())
    last_name = db.Column(db.String())

    def __init__(self, confirmation_number, first_name, last_name):
        self.confirmation_number = confirmation_number
        self.first_name = first_name
        self.last_name = last_name

class Apscheduler_Jobs(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(128))
