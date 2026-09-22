# What it does: Acts as an MQTT subscriber, subscribing to a topic and printing received messages
# Wiring:       No wiring needed (network application)
# Expected output: The connection result code and the received topic/payload are printed
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/network/mqtt

import paho.mqtt.client as mqtt

# Server and topic information
host = 'mq.tongxinmao.com'
port = 18830
topic = '/public/walnutpi/2'


# Callback executed when the client receives a CONNACK response from the server
def on_connect(client, userdata, flags, rc):
    print("Connected with result code " + str(rc))
    # Subscribing in on_connect() means the subscription is renewed if the connection is lost and restored
    client.subscribe(topic)


# Callback executed when a message published by another device is received
def on_message(client, userdata, msg):
    print(msg.topic + " " + str(msg.payload))


# Construct the MQTT client object
client = mqtt.Client()

# Configure the connection and message callbacks
client.on_connect = on_connect
client.on_message = on_message

# Connect to the broker
client.connect(host, port)

# Blocking call that processes network traffic, dispatches callbacks and handles reconnects
client.loop_forever()
