#!/bin/bash

#stop docker containers
docker stop flask_app postgres-db flask_backend bns_hackathon_backend
docker rm flask_app postgres-db flask_backend bns_hackathon_backend
docker rmi dejanualex/bns_hackathon bns_hackathon_backend