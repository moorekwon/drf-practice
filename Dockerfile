FROM    python:3.7-slim

RUN     apt -y autoremove && apt -y update && apt -y dist-upgrade
RUN     apt -y install nginx

COPY    ./requirements.txt /tmp/
RUN     pip install -r /tmp/requirements.txt

COPY    . /srv/drf-practice
WORKDIR /srv/drf-practice/app

COPY    .config/ref.nginx /etc/nginx/sites-enabled
RUN     rm /etc/nginx/sites-enabled/default

RUN     mkdir /var/log/gunicorn/

CMD     /bin/bash