<h1 align=center><strong>Gotta Guess'Em All!</strong></h1>

A Pokemon world combined with Machine Learning technology where users battle each others to become the Grandmaster of Classification Problem!

---

# Introduction

This web application is a full-stack software developed with:

* Database $\rightarrow$ PostgreSQL with Asynchronous SQLAlchemy and Alembic.
* Backend $\rightarrow$ FastAPI, Pydantic, Starlette, Uvicorn, and PyTest.
* Frontend $\rightarrow$ React JS, TypeScript, and Jest.

The URL list for the dockerized application:

    On Mac & Linux:

    * Dockerized DB Editor $\rightarrow$ `http://0.0.0.0:8081`
    * Dockerized Backend API $\rightarrow$ `http://0.0.0.0:8001/api`
    * Dockerized Backend API Dockumentation $\rightarrow$ `http://0.0.0.0:8001/docs`
    * Dockerized Frontend $\rightarrow$ `http://0.0.0.0:3001`

    On Windows

    * Dockerized DB Editor $\rightarrow$ `http://localhost:8081`
    * Dockerized Backend API $\rightarrow$ `http://localhost:8001/api`
    * Dockerized Backend API Dockumentation $\rightarrow$ `http://localhost:8001/docs`
    * Dockerized Frontend $\rightarrow$ `http://localhost:3001`

or the without docker:

* DB Editor $\rightarrow$ Depends on your machine's database editor
* Backend API $\rightarrow$ `http://localhost:8000/api`
* Backend API Dockumentation $\rightarrow$ `http://localhost:8000/docs`
* Frontend $\rightarrow$ `http://localhost:3000`

The default application's settings utilizes the `development` environment. Please change it via terminal for the needed environment:

* Development settings: `DEVELOPMENT=DEV`
* Production settings: `DEVELOPMENT=PROD`
* Staging (for testing) settings: `DEVELOPMENT=STAGE`

# Set Up Guide

#### Before the step-by-step set up, please ensure that you have:

* Docker dashboard, otherwise for Mac users run `brew install --cask docker`,
* most recent source code, otherwise execute this in your terminal `git pull --rebase origin trunk`,
* put the `env` file that is uploaded into Slack in the root directory, and
* rename `env` into `.env`.

#### Once the above preliminary requirements are fulfilled, follow these steps:

* Step 1: Give permission to the `.sh` files:

    On Mac:
    
    ```shell
    # One for backend if it exists
    chmod x+ backend/entrypoints/db.sh
    
    # One for frontend if it exists
    chmod x+ frontend/entrypoints/backend.sh
    ```
    
    
    On Windows:
    
    * Select the .sh file in VS Code
    * Change the 'Select End of Line Sequence' in the bottom bar of VS Code from 'CRFL' to 'LF'
    * Do this with both .sh files
    

* Step 2: install `pre-commit` for your working environment`

    ```shell
    pre-commit
    ```

* Step 3: Build the containers:

    ```shell
    docker-compose build
    ```

* Step 4: Generate database migration (of course if exists!):

    ```shell
    docker exec ggea_backend alembic revision --autogenerate -m "YOUR_REVISION_MESSAGE_HERE"
    docker exec ggea_backend alembic upgrade head
    ```

* Step 5: Start the containers:

    ```shell
    docker-compose up
    ```
    
    
#### The next steps are neccessary on the first start of the docker: 

When first starting the docker, you will get a error message similar to this:

    ```shell
    ggea_backend               | asyncpg.exceptions.InvalidCatalogNameError: database "ggea_dev_db" does not exist
    ```
    
Follow these steps to resolve this issue:

* Step 1: After starting the docker navigate to `http://localhost:8081/`

* Step 2: Change the Database System to -> PostgresSQL and fill in the following credentials

    ```shell
    Server: ggea_postgres_dev_server
    User: postgres
    Password: (insert the value of POSTGRES_PASSWORD of your local .env file)
    Database: (leave this field blank)
    ```
    
    Now you should be able to login!
    
* Step 3: Click on 'Create Database'

* Step 4: Insert 'ggea_dev_db' in the empy form field and click save

* Step 5: Restart your docker. Now it should run without problems!

#### Optional Steps

* Optional Step 1: Always remove your container when updating it:

    ```shell
    docker-compose down
    ```

* Optional Step 2: One step for building + starting the application:

    ```shell
    docker-compose up -d --build
    ```

Now you can go to the above URLs to find our application's page!
