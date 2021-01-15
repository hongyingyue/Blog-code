#!/usr/bin/python
import psycopg2


def connect_db():
    try:
        conn = psycopg2.connect(database="road", user="postgres", password="pass123", host="127.0.0.1", port="5432")
        print("Opened database successfully")
    except Exception as e:
        print('error')
    else:
        return conn
    return None


def close_db_connection(conn):
    conn.commit()
    conn.close()


def create_table():
    conn = connect_db()
    if not conn:
        return
    cur = conn.cursor()
    cur.execute(" CREATE TABLE IF NOT EXISTS dictionary(english VARCHAR(30), "
                "chinese VARCHAR(80), times SMALLINT, in_new_words SMALLINT)")
    close_db_connection(conn)


