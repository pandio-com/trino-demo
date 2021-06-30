<a href="https://pandio.com"><img src="https://pandio-com.github.io/static/files/assets/pandio_225_blue-05.svg" alt="Pandio Logo"></a>

# Pandio Trino Demonstration

The purpose of this repository is to give a full demonstration of Trino.

This demo runs Trino 354, MySQL, and PostgreSQL within Docker.

This demo loads test data into a MySQL database and test data into a PostgreSQL database, then executes a select across both databases in a single command.

## Requirements

Python 3.5-3.8

Docker Engine 20+

Mac OS X / Linux

## Steps

1. `git clone git@github.com:pandio-com/trino-demo.git && cd ./trino-demo`

2. Refer `.env.example` for environment variables being used, create .env file from it and change the values of those variables if necessary.

3. Open terminal window and run `./run.sh` which will run coordinator, 2 workers, postgresql and mysql inside docker containers.

4. Run `pip install -r requirements.txt` to install dependencies.

4. Open second terminal window and run `./demo.sh` which will run load-data.py file to generate some random data inside mysql and postgres db.

This will output number of rows that we've set in this env variable `LIMIT` from the random data inserted into each database.

**Note:** To stop and remove the running containers, open the terminal in the project root dir, run `TRINO_VERSION=354 docker-compose stop` to stop the running containers and `TRINO_VERSION=354 docker-compose rm` which will give prompt for the confirmation to remove the stopped containers.

## For running trino-demo inside container

1. Run `TRINO_VERSION=354 docker-compose up -d --build trino-demo` which will build the trino-demo app. Run another command `TRINO_VERSION=354 docker-compose ps` to check all containers are running. You can check the logs of all containers using `TRINO_VERSION=354 docker-compose logs -f`.

2. Open another terminal inside the same project dir and run `docker exec -it trino-demo_trino-demo_1 ./demo.sh` which will show you the output of the demo.sh script,where you can modify the demo.sh from the outside from the local and can execute that changed script using the aforementioned command.

**Note:** To stop and remove the running containers, open the terminal in the project root dir, run `TRINO_VERSION=354 docker-compose stop` which will stop all the containers which were running and further `TRINO_VERSION=354 docker-compose rm` which will give prompt for the confirmation to remove the stopped containers.
