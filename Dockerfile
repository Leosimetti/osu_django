FROM python:3.8-alpine
WORKDIR /app
COPY req.txt /app/
RUN apk update && apk add postgresql-dev gcc python3-dev musl-dev
RUN pip3 install -r req.txt
COPY . /app/
RUN python3 manage.py makemigrations
RUN python3 manage.py migrate

ENV DB_HOST=db