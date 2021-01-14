FROM python:3.6
ARG POSTGRES_HOST=localhost
ARG POSTGRES_PORT=5432
ARG POSTGRES_SCHEMA=postgres
ARG POSTGRES_PASSWORD
COPY ./requirements.txt /usr/local/
RUN pip install -r /usr/local/requirements.txt && rm -f /usr/local/requirements.txt
RUN mkdir /usr/local/app
COPY . /usr/local/app
RUN chmod -R 777 /usr/local/app
WORKDIR /usr/local/app
ENV FLASK_APP=lms
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
ENV POSTGRES_HOST=$POSTGRES_HOST
ENV POSTGRES_PORT=$POSTGRES_PORT
ENV POSTGRES_SCHEMA=$POSTGRES_SCHEMA
ENV FLASK_DEBUG=0
EXPOSE 5000
ENTRYPOINT flask run -h "0.0.0.0" -p 5000