FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . .

COPY ./db_stuff .
ENV env_name $DATABASE_URL
ENV env_name $DATABASE_USER
ENV env_name $DATABASE_PASSWORD

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST=localhost

# Expose port 5000
EXPOSE 5000

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]