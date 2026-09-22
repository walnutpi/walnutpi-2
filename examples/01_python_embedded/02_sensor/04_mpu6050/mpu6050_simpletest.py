# What it does: Reads acceleration, gyroscope and temperature from an MPU6050 6-axis sensor over I2C1
# Wiring:       Connect the MPU6050 to I2C1 (SCL1/SDA1), module address 0x68
# Expected output: Acceleration (m/s^2), gyroscope (rad/s) and temperature (C) are printed every second
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/sensor/mpu6050

import time
import board
import busio
import adafruit_mpu6050

# Construct the I2C object, controlled by WalnutPi I2C1
i2c = busio.I2C(board.SCL1, board.SDA1)

# Construct the MPU6050 object
mpu = adafruit_mpu6050.MPU6050(i2c, address=0x68)

while True:

    print("Acceleration: X:%.2f, Y: %.2f, Z: %.2f m/s^2" % (mpu.acceleration))
    print("Gyro X:%.2f, Y: %.2f, Z: %.2f rad/s" % (mpu.gyro))
    print("Temperature: %.2f C" % mpu.temperature)
    print("")

    time.sleep(1)   # Delay 1 second
