#!/bin/bash

sudo apt install memcached redis-server

sudo service redis-server start

sudo service memcached start

pip install redis python-memcached
