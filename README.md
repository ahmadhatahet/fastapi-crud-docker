# CRUD using Fastapi and Docker
Utilizing FastAPI and MariaDB to create easy to use CRUD (Create-Read-Update-Delete) API in Python.
With help of docker this project create two containers:
1. FastAPI: to maintaine the API
2. MariaDB: to host the database and perform the CRUD operations.
<br /><br />
## Steps to run the project:
1. Make sure you have docker installed :whale:
```
docker --version
```
If not please refere to the [Docker Website](https://docs.docker.com/engine/install/) and install from there.


2. Navigate to your prefered destination and clone the repository
```
git clone https://github.com/ahmadhatahet/fastapi-crud-docker.git

cd fastapi-crud-docker
```

3. start docker containers:
```
docker compose up -d
```

4. Visit: http://localhost:5404/docs

5. To ingest some sample data for the first time please visit the [migrate url](http://localhost:5404/migrate/). You will recive a response like this:
```
{'message': 'Created tables and inserted sample data successfully!'}
```

<br />

## Preview
Here is a [PDF](https://github.com/ahmadhatahet/fastapi-crud-docker/blob/master/pdf/CRUD%20using%20Fastapi%20and%20Docker.pdf) showing all CRUD operation in action.

<br />

## Note
FastAPI uses the 5404 port, if the port is already occubied in your local, kindly change the port to a prefered one in `docker-compose.yml` line `13` from `5404` to another one.