import threading
from typing import Callable
from resources.database import connect_to_database
from resources.database import fetch_all_users


def fetch_data():
    connection = connect_to_database()
    print(fetch_all_users(connection))
    connection.close()


def create_new_threads(method: Callable, num_threads: int = 1):
    # Create a list to hold the thread objects
    threads = []

    # Create the specified number of threads
    for _ in range(num_threads):
        # Create a thread object with the target function
        thread = threading.Thread(target=method)
        # Start the thread
        thread.start()
        # Add the thread object to the list
        threads.append(thread)

    # Wait for all threads to finish (optional)
    for thread in threads:
        thread.join()


# Executing and Testing

# create_new_threads(fetch_data, num_threads=3)
