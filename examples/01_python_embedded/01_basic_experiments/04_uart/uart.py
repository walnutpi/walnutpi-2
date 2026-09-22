# What it does: Sends "Hello WalnutPi!" over UART2 (/dev/ttyS2) and echoes back any data received
# Wiring:       Connect a USB-to-TTL adapter (3.3V) to UART2, cross TX/RX, common GND
# Expected output: The serial assistant receives "Hello WalnutPi!" and any data it sends is echoed back
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/gpio/uart

import serial
import time

# Configure the serial port
com = serial.Serial("/dev/ttyS2", 115200)

# Send the prompt string
com.write(b'Hello WalnutPi!')

while True:

    # Get the number of bytes waiting in the receive buffer
    count = com.inWaiting()

    if count != 0:   # Data received

        # Read the data and print it
        recv = com.read(count)
        print(recv)

        # Send the data back
        com.write(recv)

        # Flush the receive buffer
        com.flushInput()

    time.sleep(0.1)   # 100ms polling interval
