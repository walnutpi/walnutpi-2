# What it does: Reads ambient and object temperature from an MLX90614 infrared thermometer over I2C1
# Wiring:       Connect the MLX90614 to I2C1 (SCL1/SDA1), module address 0x5A
# Expected output: Ambient temperature and object temperature in Celsius are printed every second
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/sensor/mlx90614

import time
import board
import busio
import adafruit_mlx90614

# Construct the I2C object, controlled by WalnutPi I2C1
i2c = busio.I2C(board.SCL1, board.SDA1)

# Construct the MLX90614 object
mlx = adafruit_mlx90614.MLX90614(i2c, address=0x5a)

while True:

    print("Ambient Temp: ", '%.2f' % mlx.ambient_temperature)   # Ambient temperature
    print("Object Temp: ", '%.2f' % mlx.object_temperature)     # Object temperature

    time.sleep(1)   # Delay 1 second
