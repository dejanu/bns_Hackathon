#!/usr/bin/env python3

import psycopg2
import os

def create_connection(docker=False):
    if docker:
        # container name from docker-compose.yml
        host = "postgres_db"
    else:
        host = "localhost"
    # create connection to connect to database
    print(f"Connecting to database...{host}")
    connection = psycopg2.connect(
        host = host,
        database = os.environ.get('DATABASE_NAME'),
        user = os.environ.get('DATABASE_USER'),
        password = os.environ.get('DATABASE_PASSWORD')
    )
    return connection

def open_cursor():
    conn=create_connection()
    # open a cursor to perform database operations
    cur = conn.cursor()
    cur.execute("SHOW max_connections")
    print(cur.fetchone())
    return cur

def close_cursor(cursor_name, connection_name):
    # close named cursor and connection
    cursor_name.close()
    connection_name.close()

def run_script(script_name):
    with open (script_name, "r") as script_file:
        sql_script = script_file.read()
    conn = create_connection()
    with conn.cursor() as cur:
        cur.execute(sql_script)
        conn.commit()
    close_cursor(cur,conn)

if __name__ == "__main__":
    run_script("create_table.sql")