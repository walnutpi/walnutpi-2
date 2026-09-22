# What it does: Toggles a relay on PB6 every time the onboard KEY button is pressed
# Wiring:       Connect the relay control pin to PB6
# Expected output: Each KEY press flips the relay state
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/module/relay

import board
import time
from digitalio import DigitalInOut, Direction

# Construct relay object and initialize
relay = DigitalInOut(board.PB6)       # Define pin number
relay.direction = Direction.OUTPUT    # IO as output
relay.value = 1                       # Turn off the relay at startup

# Construct KEY object and initialize
switch = DigitalInOut(board.KEY)      # Define pin number
switch.direction = Direction.INPUT    # IO as input

state = 1   # Relay initial state, high level turns it off

while True:

    if switch.value == 0:             # Key pressed
        time.sleep(0.01)              # Debounce: wait 10ms
        if switch.value == 0:         # Confirm the key is pressed

            state = not state         # Toggle the state
            relay.value = state       # Change the relay state

            # Wait for the key to be released
            while switch.value == 0:
                pass
