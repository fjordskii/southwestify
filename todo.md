Successfully adds flights both ways now but can make infinite requests, need to address at some point with user data

Need to add SSL cert

Fix 'schedule check-in' button look and feel

add job id to User db object in firebase

Need to add NGINX next

Do Cache stuff for static assets

Check if only scheduling for first flight

Map User to AP Job probably in PostgreSQL















for successful bookings, switch to Firebase records instead of query params
  - Working
  - Need to connect Users to Flights via FK

- switch to uWSGI server
- implement NGINX

TypeError: 'NoneType' object is not subscriptable

It's sending emails for both outbound and inbound flights

Have fail-safe if can't find check-in request
- just prints

Add loading spinner while Vue makes request to add job

Need to capitalize names/strip white space of forms

potentially need to add CSRF fixes

need to figure out how to actually grab last vue build

persist vue login sessions

create .dockerignore file, remove sensitive info from dockerfile as well

definitely need heroku.yml file - offloads docker build to heroku
