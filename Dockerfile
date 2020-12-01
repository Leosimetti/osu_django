FROM python:3.8
WORKDIR /app
COPY req.txt /app/
#RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip install -r req.txt
COPY . /app/

ENV DB_HOST=db

RUN python manage.py makemigrations
RUN python manage.py migrate
