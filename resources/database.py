import sqlite3

'''Here is a database module'''


def connect_to_database():
    # establishing db connection
    connection = sqlite3.connect("goods.db")
    return connection


def execute_query(connection, query):
    cursor = connection.cursor()
    cursor.execute(query)
    return cursor.fetchall()


def fetch_all_users(connection):
    cursor = connection.cursor()
    query = """SELECT * from users"""
    cursor.execute(query)
    return cursor.fetchall()


def close_connection(connection):
    connection.close()
