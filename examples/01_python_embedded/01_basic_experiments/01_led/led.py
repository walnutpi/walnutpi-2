# What it does: Turns on the onboard blue LED
# Wiring:       No wiring needed (onboard LED on PC13)
# Expected output: The onboard blue LED lights up
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/gpio/led

import board
from digitalio import DigitalInOut, Direction

# Construct LED object and initialize
led = DigitalInOut(board.LED)       # Define pin number
led.direction = Direction.OUTPUT    # IO as output

led.value = 1   # Output high level, turn on the onboard blue LED

# led.value = 0   # Output low level, turn off the onboard blue LED
