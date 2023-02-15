# Adminer

## Introduction

Adminer is a PHP-based database management tool. What makes it special is their Docker Image that we set up in `./docker-compose.yaml`. Read more about it here: [Adminer](https://www.adminer.org/)

For this project, we set up 2 adminer database editors:

* `ggea_dev_db_editor` $\rightarrow$ Activated when `ENVIRONMENT=DEV`
* `ggea_test_db_editor` $\rightarrow$ Activated when `ENVIRONMENT=STAGE`

## Development Database

Both database editors have the same login credentials, only the following inputs need to be changed respectively:

* System $\rightarrow$ PostgreSQL
* Server $\rightarrow$ `ggea_postgres_dev_server`
* Database $\rightarrow$ `ggea_dev_db_editor`

## Testing Database

Please change the following inputs:

* System $\rightarrow$ PostgreSQL
* Server $\rightarrow$ `ggea_postgres_test_server`
* Database $\rightarrow$ `ggea_test_db_editor`

---
