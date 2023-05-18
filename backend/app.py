#!/usr/bin/env python3

import psycopg2
import os

from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

# from db_stuff.create_db import create_connection, close_cursor, run_script

app = Flask(__name__) 
app.config["DEBUG"] = True

# connect to postgres database psycopg2 PostgreSQL adapter
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')

# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

with app.app_context():
    # create connection and instert data to the database
    connection = psycopg2.connect(
        host = "postgres_db",
        database = os.environ.get('DATABASE_NAME'),
        user = os.environ.get('DATABASE_USER'),
        password = os.environ.get('DATABASE_PASSWORD')
    )
    with open ('db_stuff/create_table.sql', "r") as script_file:
        sql_script = script_file.read()
    with connection.cursor() as cur:
        cur.execute(sql_script)
        connection.commit()
        cur.close()
    connection.close()
 

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    """ search name object in the database """
    name = request.form['name']
    db_query = "SELECT * FROM kubernetes WHERE kobj='{}';".format(name)
    
    connection = psycopg2.connect(
        host = "postgres_db",
        database = os.environ.get('DATABASE_NAME'),
        user = os.environ.get('DATABASE_USER'),
        password = os.environ.get('DATABASE_PASSWORD')
    )
    with connection.cursor() as cur:
        cur.execute(db_query)
        result = cur.fetchone()
        cur.close()
    connection.close()
    return render_template('submit.html', name=name, result=result)

if __name__ == '__main__':
    app.run(debug=True)
