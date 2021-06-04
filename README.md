# API with two endpoints(docker-compose)
## Test case

API (FastAPI, sqlalchemy core, alembic)

### API Endpoints

#### List of endpoints

* **/api/v1/loans** (POST: create a loan with url parameter product_name)
* **/api/v1/loans/{product_uuid}** (GET: get a loan by uuid)

#### Auto generated swagger docs
* **/docs**

You may need to change files with your username and password for postgres:
* **alembic.ini**
* **setting.py**
* **env.py**
* **docker-compose.yml**

### How to launch 
    docker-compose up --build
    docker-compose run app alembic revision --autogenerate -m "Name of your migration"
    docker-compose run app alembic upgrade head
    docker-compose up
    

