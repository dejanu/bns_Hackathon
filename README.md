# bns_Hackathon

- DevPost Profile [dejanualex](https://devpost.com/dejanu)
- Hackathon [BNS Hackathon](https://bunnyshell.devpost.com/resources)


## Project Description

* If you want to rename the `app.py` file, e.g. `mv app.py main.py`, you need to update env variable `FLASK_APP` `export FLASK_APP=main.py`
```bash
# default port 5000
flask run --host=0.0.0.0
``` 

* Docker:
```bash
docker build -t dejanualex/bns_hackathon .

# start flask app as docker container
docker run -p 5000:5000 dejanualex/bns_hackathon

# start docker compose (currently only database)
docker-compose -f docker-compose.yml up --remove-orphans

# create env vars
source db_stuff/setup_db.sh

# populate database with test data
./create_db.py 
```
