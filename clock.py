'''
    Title: Python Console Clock
    Author: Michael Valdron
    Date: 04-20-2016
'''
from datetime import datetime
import time
import os

# Sets the screen clear call
clear = lambda: os.system("clear")

# Sets the current time value
current_time = datetime.now()

try:
    while True:
        # Refreshes the frame
        clear()

        # Displays the current frame
        print "%s:%s:%s" % (str(current_time.hour).zfill(2), str(current_time.minute).zfill(2), str(current_time.second).zfill(2))

        # Waits a second
        time.sleep(1)

        # Gets the current time
        current_time = datetime.now()

except KeyboardInterrupt:
    # Refreshes the frame
    clear()
