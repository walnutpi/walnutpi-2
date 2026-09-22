# What it does: Turns on the onboard blue LED while the onboard KEY button is held down
# Wiring:       No wiring needed (onboard LED and onboard KEY button)
# Expected output: The LED lights up while KEY is pressed and turns off when released
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/gpio/key

import board
from digitalio import DigitalInOut, Direction, Pull

# Construct LED object and initialize
led = DigitalInOut(board.LED)       # Define pin number
led.direction = Direction.OUTPUT    # IO as output

# Construct KEY object and initialize
key = DigitalInOut(board.KEY)       # Define pin number
key.direction = Direction.INPUT     # IO as input
key.pull = Pull.UP                  # Enable the pull-up resistor

while True:

    if key.value == 0:   # Key pressed
        led.value = 1    # Turn on the LED

    else:                # Key released
        led.value = 0    # Turn off the LED
