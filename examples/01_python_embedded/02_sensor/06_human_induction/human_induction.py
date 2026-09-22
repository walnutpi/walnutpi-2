# What it does: Turns on the onboard blue LED when a human infrared sensor detects a person
# Wiring:       Connect the sensor signal pin to PB6
# Expected output: The LED turns on when a person is detected and off otherwise, checked every 0.5 second
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/sensor/human_induction

import time
import board
from digitalio import DigitalInOut, Direction

# Construct the human infrared sensor object, the pin is PB6
human = DigitalInOut(board.PB6)     # Define pin number
human.direction = Direction.INPUT   # IO as input

# Construct LED object and initialize
led = DigitalInOut(board.LED)       # Define pin number
led.direction = Direction.OUTPUT    # IO as output

while True:

    if human.value == 1:   # Person detected
        led.value = 1      # Turn on the LED

    else:                  # No person
        led.value = 0      # Turn off the LED

    time.sleep(0.5)        # Detection interval, 0.5 second
