FROM python:3.6
RUN pip install Flask
RUN pip install SQLAlchemy
RUN pip install psycopg2
RUN mkdir /usr/local/app
COPY . /usr/local/app
WORKDIR /usr/local/app
RUN chmod -R 777 /usr/local/app
ENV FLASK_APP=lms
ENTRYPOINT flask run