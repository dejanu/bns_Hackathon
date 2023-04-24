#!/usr/bin/env python3
import os 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

from db_stuff.create_db import create_connection, open_cursor, close_cursor


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
    """ get the number of connections to the database """
    # create a connection to the database
    conn = create_connection(docker=True)
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM kubernetes WHERE kobj='pod';")
        row = cur.fetchone()
    # close cursor and connection
    close_cursor(cur,conn)
    print(row[0])
    return f"Pod object: {row}"

@app.route('/')
def home():
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    name = request.form['name']
    # do something with the data
    return render_template('submit.html', name=name)

if __name__ == '__main__':
    app.run(debug=True)
