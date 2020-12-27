FROM python:3.6
RUN pip install Flask
RUN pip install SQLAlchemy
RUN pip install psycopg2
COPY ./rest_service.py /usr/local/rest_service.py
RUN chmod 777 /usr/local/rest_service.py
ENV FLASK_APP=/usr/local/rest_service.py
ENTRYPOINT flask run