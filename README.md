# bns_Hackathon

- DevPost Profile [dejanualex](https://devpost.com/dejanu)
- Hackathon [BNS Hackathon](https://bunnyshell.devpost.com/resources)


## Project Description

* If you want to rename the `app.py` file, e.g. `mv app.py main.py`, you need to update env variable `FLASK_APP` `export FLASK_APP=main.py`
```bash
# default port 5000
flask run --host=0.0.0.0
``` 

* Docker setup:
```bash

# create env vars
source db_stuff/setup_db.sh

docker build -t dejanualex/bns_hackathon .

# start flask app as docker container
docker run -p 5000:5000 -e DATABASE_URL=$DATABASE_URL -e DATABASE_USER=$DATABASE_USER -e DATABASE_PASSWORD=$DATABASE_PASSWORD dejanualex/bns_hackathon

# start docker compose (currently only database)
docker-compose -f docker-compose.yml up --remove-orphans


# populate database with test data
./create_db.py 
```
* Bunyshell sutff:

- [env_definition](https://documentation.bunnyshell.com/docs/environment-definition)

- [env_deployment](https://documentation.bunnyshell.com/docs/quickstart-dockercompose-deploy-the-environment)

- [docker compose documentation](https://documentation.bunnyshell.com/docs/components-docker-compose)