FROM postgres
ARG POSTGRES_PASSWORD
ENV POSTGRES_PASSWORD=$POSTGRES_PASSWORD
COPY init.sql /docker-entrypoint-initdb.d/
