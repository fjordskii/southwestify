Have fail-safe if can't find check-in request

need to figure out how to actually grab last vue build

persist vue login sessions

switch to uWSGI server

for successful bookings, switch to PostgreSQL records instead of query params

re-implement email through firebase functions

create .dockerignore file, remove sensitive info from dockerfile as well



BLOCKED:
- Step 1) push docker image to heroku but need to connect to heroku's postgres instance which is:
  `postgresql://jnjuqjgkicxtyz:4d4f82ef1239f2be51e37208bda68e7b5e53e11701774e2d5c771aa5de435278@ec2-35-168-54-239.compute-1.amazonaws.com/d5niq3ngvr9fkb`
- Step 2) definitely need heroku.yml file - offloads docker build to heroku
- need to redo configs etc
