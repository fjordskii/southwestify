# Welcome to Southwestify/Pyschedule!

Provides an ability for users to schedule their Southwest flight check-ins. 

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
  
  
  Current known bugs/issues:
  - Jobs are currently tied to CST time only, need to change this to global UTC
  - Jobs may or may not be only scheduling for the first leg of a roundtrip flight, need to investigate
  - Need to clean up UI/UX/Copy
  - Google sign in doesn't work in mobile, need to switch to different firebase login method
  - Need to add code coverage to Vue components
