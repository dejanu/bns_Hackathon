#!/usr/bin/env python3
import os
import psycopg2
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__) 
app.config["DEBUG"] = True
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
# initialize the app with the extension
db = SQLAlchemy()
db.init_app(app)

def create_connection():
    """ create a database connection to a PostgreSQL database """
    connection = None
    try:
        connection = psycopg2.connect(
            host = "db",
            database = os.environ.get('DATABASE_NAME'),
            user = os.environ.get('DATABASE_USER'),
            password = os.environ.get('DATABASE_PASSWORD')
        )
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    return connection

@app.route('/')
def populate_db():
    """ populate database with test data """
    connection = create_connection()
    cursor = connection.cursor()
    # execute the sql query
    with open (f"{os.getcwd()}/db_stuff/create_table.sql", "r") as script_file:
        sql_script = script_file.read()
        cursor.execute(sql_script)
        connection.commit()
    # close the cursor and connection
    cursor.close()
    connection.close()
    return render_template('form.html')

@app.route('/submit', methods=['POST'])
def submit():
    """ search name object in the database """
    name = request.form['name'].lower()
    db_query = f"SELECT * FROM kubernetes WHERE kobj='{name}';"
    connection = create_connection()
    with connection.cursor() as cur:
        cur.execute(db_query)
        result = cur.fetchone()
        cur.close()
    connection.close()
    return render_template('submit.html', name=name, result=result)

if __name__ == '__main__':
    app.run(debug=True)
