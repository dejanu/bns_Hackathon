#!/bin/bash

#stop docker containers
docker stop flask_backend postgresdb
docker rm flask_backend postgresdb
docker rmi dejanualex/bns_hackathon bns_hackathon_backend postgres:15.3