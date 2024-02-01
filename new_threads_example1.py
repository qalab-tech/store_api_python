from resources.database import connect_to_database
from resources.database import execute_query
from resources.database import close_connection
import threading
import time

def retrieve_data():
    connection = connect_to_database()
    print('Connection Established')
    query = """SELECT * from users"""
    users = execute_query(connection, query)
    for user in users:
        print(user)
    close_connection(connection)

def update_data():
    connection = connect_to_database()
    print('Connection Established')
    query = """UPDATE users SET name = "JuliaRoberts" WHERE id = 3"""
    execute_query(connection, query)
    connection.commit()
    close_connection(connection)

# Create 5 threads with different methods
threads = []
methods = [retrieve_data, update_data]  # List of methods to be executed by each thread

for method in methods:
    thread = threading.Thread(target=method)
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

