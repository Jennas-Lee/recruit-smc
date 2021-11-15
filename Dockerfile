FROM python:3.10.0-bullseye

WORKDIR /app

ADD . /app/

RUN python -m pip install --upgrade pip
RUN pip install --upgrade setuptools
RUN pip install -r requirements.txt
RUN pip install psycopg2
RUN pip install uwsgi

EXPOSE 8000
#CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
CMD ["uwsgi", "-i", "/app/uwsgi/uwsgi.ini", "--http", ":8000"]