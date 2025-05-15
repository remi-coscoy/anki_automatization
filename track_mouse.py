from autopy import mouse
import time

try:
    while True:
        x, y = mouse.location()
        print(f"Mouse position: ({x}, {y})", end="\r")  # Overwrites the same line
        time.sleep(0.1)
except KeyboardInterrupt:
    print("\nTracking stopped.")
