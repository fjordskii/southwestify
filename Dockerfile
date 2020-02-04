# build
FROM node:11.12.0-alpine as build-vue
WORKDIR /app/client
ENV PATH /app/node_modules/.bin:$PATH
COPY ./client/package*.json ./
RUN npm install
COPY ./client .
RUN npm run build

FROM python:3.6
# FROM python:3.8.0-alpine
WORKDIR /app

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

ADD . /app
RUN pip install --trusted-host pypi.python.org -r requirements.txt
EXPOSE 5000

# execute the Flask app
CMD ["python", "app.py"]
