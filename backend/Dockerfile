FROM python:3.8-slim-buster

WORKDIR /app
COPY requirements.txt requirements.txt
RUN pip3 install --no-cache-dir -r requirements.txt

COPY . /app
# envs to be passed in at runtime with --env
ENV DATABASE_URL=${DATABASE_URL}
ENV DATABASE_USER=${DATABASE_USER} 
ENV DATABASE_PASSWORD=${DATABASE_PASSWORD}

ENV FLASK_APP app.py
ENV FLASK_RUN_HOST=0.0.0.0

# Expose port 5000
EXPOSE 5000

CMD ["python3", "-m" , "flask", "run", "--host=0.0.0.0"]