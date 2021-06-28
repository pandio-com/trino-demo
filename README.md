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

2. Refer `.env.example` for environment variables being used, change the values of those variables if necessary and export those.

3. Open terminal window and run `./run.sh`

4. Run `pip install -r requirements.txt` to install dependencies

4. Open second terminal window and run `./demo.sh` which will run coordinator, 2 workers, postgresql and mysql inside docker containers.

This will output number of rows that we've set in this env variable `LIMIT` from the random data inserted into each database.

**Note:** To shutdown, exit the first terminal running `./run.sh`

## For running trino-demo inside container

1. Uncomment `trino-demo` service configuration inside docker-compose.yaml.

2. Run `docker-compose up --build` which will build the trino-demo app.

This will output number of rows that we've set in this env variable inside docker-compose.yaml file `LIMIT` from the random data inserted into each database.

**Note:** To shutdown, exit the first terminal with `Ctrl+C`

**Note:** To remove the stopped containers, run `docker-compose rm -f`
