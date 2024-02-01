from resources import database as db
from resources.app_logger import logger
from resources import multythreads as mu
from resources.database import fetch_all_users
def main():
    connection = db.connect_to_database()
    logger.info("Connected to the Database")

    mu.create_new_threads(fetch_all_users(connection), num_threads=4)
    logger.info("Data fetched successfully.")
    # for user in users:
    #     user_name = user[1]
    #     user_age = user[2]
    #     logger.info(f'User {user_name} is {user_age} years old.')
    db.close_connection(connection)
    logger.info("Connection closed successfully.")


    #users = db.fetch_all_users(connection)
    # # connection = db.connect_to_database()
    # logger.info("Connection to SQLite Database Established.")
    # # query = """SELECT * FROM users"""
    # # users = db.execute_query(connection, query)
    # users = db.fetch_all_users(connection)

    # for user in users:
    #     user_name = user[1]
    #     user_age = user[2]
    #     print(f'User {user_name} is {user_age} years old.')
    # logger.info("Data fetched successfully.")
    #
    # db.close_connection(connection)
    # logger.info("Connection closed successfully.")


if __name__ == '__main__':
    main()
