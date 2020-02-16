from app import db

class Apscheduler_Jobs(db.Model):
    __tablename__ = "apscheduler_jobs"

    id = db.Column(db.Integer, primary_key=True)
    next_run_time = db.Column(db.String(128))
    job_state = db.Column(db.String(128))

    def __init__(self, name, next_run_time, job_state):
        self.name = name
        self.next_run_time = next_run_time
        self.job_state = job_state
