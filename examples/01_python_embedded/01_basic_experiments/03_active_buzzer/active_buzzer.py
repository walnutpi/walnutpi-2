# What it does: Drives an active buzzer on PI13, beeping 5 times
# Wiring:       Connect the active buzzer signal pin to PI13
# Expected output: The buzzer sounds for 0.5s and stays silent for 0.5s, repeated 5 times
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/gpio/active_buzzer

import board
import time
from digitalio import DigitalInOut, Direction

# Construct buzzer object and initialize
active_buzzer = DigitalInOut(board.PI13)     # Define pin number
active_buzzer.direction = Direction.OUTPUT   # IO as output

for i in range(5):

    active_buzzer.value = False   # Output low level, turn on the buzzer
    time.sleep(0.5)               # Delay 0.5 second

    active_buzzer.value = True    # Output high level, turn off the buzzer
    time.sleep(0.5)               # Delay 0.5 second
