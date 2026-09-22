# What it does: Acts as a TCP socket client, sending a test message and echoing back received data
# Wiring:       No wiring needed (network application)
# Expected output: Received data is printed and sent back to the server
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/network/socket

import socket
import time

# Construct the socket object
s = socket.socket()

addr = ('192.168.2.119', 10000)   # Server IP address and port
s.connect(addr)

# Send the test message
s.send(b'Hello WalnutPi!')

while True:

    text = s.recv(128)   # Receive up to 128 bytes at a time

    # Nothing received
    if text == b'':
        pass

    # Data received, print it and send it back
    else:
        print(text)
        s.send(text)

    time.sleep(0.1)   # 100ms polling interval
