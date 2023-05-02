#!/usr/bin/env python3
import os 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from db_stuff.create_db import create_connection, open_cursor, close_cursor, run_script

app = Flask(__name__)
app.config["DEBUG"] = True

#connect to postgres database psycopg2 PostgreSQL adapter
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# create the extension
db = SQLAlchemy()
# initialize the app with the extension
db.init_app(app)

# create a new route named database
@app.route('/database')
def database():
    """ create table in the database """
    # create a connection to the database
    conn = create_connection(docker=True)
    run_script('db_stuff/create_table.sql', conn)
    conn.close()
    return render_template('database.html')

@app.route('/search')
def search():
    """ search object in the database """
    conn = create_connection(docker=True)
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM kubernetes WHERE kobj='pod';")
        row = cur.fetchone()
    close_cursor(cur, conn)
    return render_template('search.html', row=row)

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    """ search name object in the database """
    name = request.form['name']
    conn = create_connection(docker=True)
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM kubernetes WHERE kobj='pod';")
        result = cur.fetchone()
    close_cursor(cur, conn)
    return render_template('submit.html', name=name, result=result)

if __name__ == '__main__':
    app.run(debug=True)
