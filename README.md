# gpx2spatialite

A script for importing GPX files into a SpatiaLite database.

## Usage

    python ./gpx2spatialite -d <path/to/database> <path/to/gpx> <user_id>


## CityDefs

Import/update citydefs into existing database:

    python extras/citydefs_tool.py -i <path/to/database> extras/insert_citydefs.sql

Export citydefs table:

    python extras/citydefs_tool.py -e <path/to/database> extras/insert_citydefs.sql

## Unit tests

Install `pytest` with the command

    sudo easy_install pytest

Run unit tests by executing the following command in the root directory

    py.test
