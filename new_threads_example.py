import threading
import time

# Define a function that will be executed in a thread
def print_numbers():
    for i in range(5):
        print(i)
        time.sleep(1)  # Simulate some work

# Create a thread object with the target function
thread = threading.Thread(target=print_numbers)

# Start the thread
thread.start()

# Wait for the thread to finish (optional)
thread.join()

print("Thread finished")