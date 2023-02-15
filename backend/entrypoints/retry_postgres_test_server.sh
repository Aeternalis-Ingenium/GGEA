#!/bin/bash

echo "Postgres Test Server --- Connecting . . ."

while ! nc -z ggea_postgres_test_server 5432; do

    echo "Postgres Test Server -- Failed!"

    sleep 1

    echo "Postgres Test Server -- Reconnecting . . ."

done

echo "Postgres Test Server --- Successfully Connected!"

exec "$@"
