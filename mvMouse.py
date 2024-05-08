import pyautogui
import time
import random

# Define the time duration (in seconds)
duration = 1000

# Get the current time
start_time = time.time()

# Define the range
start = 1
end = 1000

# Start the loop
while time.time() - start_time < duration:
    # Move the mouse pointer to a new position
    pyautogui.moveTo(100, 100, duration=2)
    # Generate a random number within the range
    random_number = random.randint(start, end)
    pyautogui.moveTo(random_number, random_number, duration=1)

    # Pause the execution for 1 second
    time.sleep(2)
