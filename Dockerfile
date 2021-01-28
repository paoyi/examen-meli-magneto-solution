FROM tiangolo/uwsgi-nginx-flask:python3.8

COPY ./MagnetoApi /app

WORKDIR /app

RUN pip install -r requirements.txt