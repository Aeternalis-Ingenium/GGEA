#!/bin/bash

echo " Postgres Development Server --- Connecting . . ."

while ! nc -z ggea_postgres_dev_server 5432; do

    echo " Postgres Development Server -- Failed!"

    sleep 1

    echo " Postgres Development Server -- Reconnecting . . ."

done

echo " Postgres Development Server --- Successfully Connected!"

exec "$@"
