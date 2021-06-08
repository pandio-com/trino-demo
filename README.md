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

1. Open terminal window and run `./run.sh`

1. Open second terminal window and run `./demo.sh`

This will output 10 rows from the random data inserted into each database.

**Note:** To shutdown, exit the first terminal running `./run.sh`

