from resources.database import connect_to_database
from resources.database import execute_query
from resources.database import close_connection
import threading
import time

print('Connection Established')


def retrieve_data():
    connection = connect_to_database()
    query = """SELECT * from users"""
    users = execute_query(connection, query)
    for user in users:
        print(user)
    close_connection(connection)


# Create 5 threads
threads = []
for _ in range(5):
    thread = threading.Thread(target=retrieve_data)
    threads.append(thread)

# Start the threads
start_time = time.time()
for thread in threads:
    thread.start()

# Wait for all threads to finish (optional)
for thread in threads:
    thread.join()

print("All threads finished")
stop_time = time.time()

execution_time = stop_time - start_time

print(f'All threads executed in {execution_time} seconds')
