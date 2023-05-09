#!/usr/bin/env python3

import time
import sys

print('Initializing robot')

duration = 10
if len(sys.argv) >= 2:
    try:
        duration = int(sys.argv[1])
    except:
        duration = 10

print(f"Robot is operational: script will now block for {duration} seconds")

time.sleep(duration)
print('Shutting down')

