#!/bin/bash

#stop all containers using their id
docker stop $(docker ps -q) 

# remove all stopped containers
docker rm -f $(docker ps -aq -f  status=exited) 

# remove all images
docker rmi -f $(docker images -a -q)