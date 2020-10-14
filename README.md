# Dating social network.

## Basic functions.


Simple registration by form and Google Auth.

Editing profile and downloading media content.

Creating blog posts with media.

Real-time chating with the people online. 

Video-audio broadcasting via WebRTC. 

Browsing people online and contact list on the chat page. 

Geting the different types of notifications about new messages, likes and others.

Profile searching.

## Commertial functions.

Replanishing account of a male.

Charging credits for different services like chat, private photo and so on.

History of payments.

Comission for femails.


## Architecture.

Project will be a monolite and contains backend and frontend in one repo.

### Frontend Angular (JS TypeScript).

1. web app (pure Angular)

2. mobile app (Ionic)


### Backend Python.

Django Rest Framework - for the REST API

Django channels - for the web-sockets

WebRTC - for the broadcasting


# Deploy backend

## System requirements

    sudo apt-get install libpq-dev redis-server

Cloning.

    git clone git@github.com:zdimon/just-dating.git
    cd just-dating

Create virtual environment.

    python3 -m venv venv
    . ./venv/bin/activate

Install requirements.

    pip3 install -r requirements.txt

Load data

    ./bin/seeddb

Run server 

    ./bin/run

## Frontend builder

    ./bin/build_mobi

## Links

swagger - http://localhost:7777

admin - http://localhost:7777/admin

mobile app - http://localhost:7777/mobi


## Nginx configuration for websocket

        location / {
            proxy_pass  http://localhost:7777;

            proxy_http_version 1.1;
            proxy_set_header Upgrade $http_upgrade;
            proxy_set_header Connection "upgrade";

            proxy_redirect off;
            proxy_set_header Host $host;
            proxy_set_header X-Real-IP $remote_addr;
            proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
            proxy_set_header X-Forwarded-Host $server_name;

        }















