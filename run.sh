#!/usr/bin/bash
docker-compose build
docker-compose down -v
docker-compose up
