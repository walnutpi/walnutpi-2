# What it does: Acts as an MQTT publisher, publishing "Hello WalnutPi!" to a topic
# Wiring:       No wiring needed (network application)
# Expected output: The message is published to the broker once per second
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/network/mqtt

import paho.mqtt.client as mqtt
import time

# Server and topic information
host = 'mq.tongxinmao.com'
port = 18830
topic = '/public/walnutpi/1'

# Construct the MQTT client object
client = mqtt.Client()

# Connect to the broker
client.connect(host, port)

while True:

    # Publish the message
    client.publish(topic, 'Hello WalnutPi!')

    time.sleep(1)   # Delay 1 second, sending interval
