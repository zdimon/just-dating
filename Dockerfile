FROM python:3 as django
ENV PYTHONUNBUFFERED 1
RUN mkdir /app
WORKDIR /app
COPY requirements.txt /app
RUN python -m pip install --upgrade pip
RUN pip install -r requirements.txt
COPY . /app/
WORKDIR /app/backend
RUN python3 manage.py migrate

FROM node:12 as node
RUN mkdir /app
COPY frontend /app/
WORKDIR /app
RUN npm install