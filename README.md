# bns_Hackathon

- DevPost Profile [dejanualex](https://devpost.com/dejanu)
- Hackathon [BNS Hackathon](https://bunnyshell.devpost.com/resources)


## Project Description

* Webapp that allows to search k8s objects definition and usage

## Deployment

* If you want to rename the `app.py` file, e.g. `mv app.py main.py`, you need to update env variable `FLASK_APP` `export FLASK_APP=main.py`
```bash
# run app on default port 5000
flask run --host=0.0.0.0
``` 

* Docker setup:
```bash
# create env vars
source backend/db_stuff/setup_db.sh

# build image and start flask app as container
docker build -t dejanualex/bns_hackathon .
docker run -p 5000:5000 -e DATABASE_URL=$DATABASE_URL -e DATABASE_USER=$DATABASE_USER -e DATABASE_PASSWORD=$DATABASE_PASSWORD dejanualex/bns_hackathon

# stop containers and remove images
./cleanup_images.sh

# start docker compose
docker-compose -f docker-compose.yml up --remove-orphans --build
```
## Bunyshell stuff:

* Each Environment has all its Docker-compose Components deployed into its own Kubernetes namespace, isolated from other environments.

- [env_definition](https://documentation.bunnyshell.com/docs/environment-definition)

- [env_deployment](https://documentation.bunnyshell.com/docs/quickstart-dockercompose-deploy-the-environment)

- [docker compose documentation](https://documentation.bunnyshell.com/docs/components-docker-compose)