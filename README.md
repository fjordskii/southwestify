# Welcome to Southwestify/Pyschedule!

This application provides an ability for users to schedule their Southwest flight check-ins months in advance (so they don't forget and get a crappy seat!). 

Long story short, there's a thin client that ultimately 
  - POSTs to `/schedule-flight-form` 
  - which then queries SW's API (via mobile user agent mocking) and 
  - finally schedules a `job` via the python `APScheduler` library
  
  That job will then be ran sometime in the future exactly 24hrs prior to the scheduled flight's departure time.
  
  
  Architecture notes:
  - Uses Google Firebase for Authentication
  - Uses SendGrid.com for email notifications
  - Uses Heroku for deployment
  - Uses Heroku PostgreSQL instance as a Job store for APScheduler Jobs
  - Is deployed as a Container via the Dockerfile (docker-compose is ultimately not used in production)
  - Uses Flask framework for backend
  - Uses Vue and Vuetify for frontend
  - Uses Gunicorn for an application server
  
  
  Current known bugs/issues:
  - Jobs are currently tied to CST time only, need to change this to global UTC
  - Jobs may or may not be only scheduling for the first leg of a roundtrip flight, need to investigate
  - Need to clean up UI/UX/Copy
  - Google sign in doesn't work in mobile, need to switch to different firebase login method
  - Need to add code coverage to Vue components
  - Need to add NGINX as a web server to more efficiencly serve static assets as the application grows.
