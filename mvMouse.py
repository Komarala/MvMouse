import pyautogui
import time

# Define the time duration (in seconds)
duration = 1000

# Get the current time
start_time = time.time()

# Start the loop
while time.time() - start_time < duration:
    # Move the mouse pointer to a new position
    pyautogui.moveTo(100, 100, duration=1)
    pyautogui.moveTo(700, 700, duration=1)

    # Pause the execution for 1 second
    time.sleep(1)
