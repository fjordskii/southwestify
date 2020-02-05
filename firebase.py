import pyrebase
import os

# api: AIzaSyCV2UXZjOC_JLMiZyogqQ-B5yPSJnsU-7g
# db secret: BR07iThHKidpJjvhtg0OjELkTjnB912sjoiOHtVU

config = {
  "apiKey": os.environ['FIREBASE_API_KEY'],
  "authDomain": "schedule-my-flight-checkin.firebaseapp.com",
  "databaseURL": "https://schedule-my-flight-checkin.firebaseio.com",
  "storageBucket": "schedule-my-flight-checkin.appspot.com"
}

firebase = pyrebase.initialize_app(config)

# db = firebase.database()
auth = firebase.auth()
