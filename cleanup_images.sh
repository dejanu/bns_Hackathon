#!/bin/bash

#stop docker containers
docker stop flask_app postgres_db
docker rm flask_app postgres_db
docker rmi dejanualex/bns_hackathon bns_hackathon_backend