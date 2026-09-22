# What it does: Reads temperature, pressure and altitude from a BMP280 barometric sensor over I2C1
# Wiring:       Connect the BMP280 to I2C1 (SCL1/SDA1), module address 0x76
# Expected output: Temperature (C), pressure (hPa) and altitude (m) are printed every second
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/sensor/bmp280

import time
import board
import busio
import adafruit_bmp280

# Construct the I2C object, controlled by WalnutPi I2C1
i2c = busio.I2C(board.SCL1, board.SDA1)

# Construct the BMP280 object, the module I2C address is the default 0x76
bmp280 = adafruit_bmp280.Adafruit_BMP280_I2C(i2c, address=0x76)

# Local sea level standard atmospheric pressure
bmp280.sea_level_pressure = 1013.25

while True:

    print("\nTemperature: %0.1f C" % bmp280.temperature)
    print("Pressure: %0.1f hPa" % bmp280.pressure)
    print("Altitude = %0.2f meters" % bmp280.altitude)

    time.sleep(1)   # Delay 1 second
