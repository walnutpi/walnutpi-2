# What it does: Measures distance with a VL53L1X time-of-flight laser ranging sensor over I2C1
# Wiring:       Connect the VL53L1X to I2C1 (SCL1/SDA1), module address 0x29
# Expected output: Sensor information is printed once, then the distance in cm is printed continuously
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/sensor/vl53l1x

import time
import board
import busio
import adafruit_vl53l1x

# Construct the I2C object, controlled by WalnutPi I2C1
i2c = busio.I2C(board.SCL1, board.SDA1)

# Construct the VL53L1X object
vl53 = adafruit_vl53l1x.VL53L1X(i2c, address=0x29)

# Parameter settings
vl53.distance_mode = 1    # 1: short distance mode; 2: long distance mode
vl53.timing_budget = 100  # Ranging duration, unit is ms

# Sensor information
print("VL53L1X Simple Test.")
print("--------------------")
model_id, module_type, mask_rev = vl53.model_info
print("Model ID: 0x{:0X}".format(model_id))
print("Module Type: 0x{:0X}".format(module_type))
print("Mask Revision: 0x{:0X}".format(mask_rev))
print("Distance Mode: ", end="")
if vl53.distance_mode == 1:
    print("SHORT")
elif vl53.distance_mode == 2:
    print("LONG")
else:
    print("UNKNOWN")
print("Timing Budget: {}".format(vl53.timing_budget))
print("--------------------")

# Start ranging
vl53.start_ranging()

while True:

    if vl53.data_ready:
        print("Distance: {} cm".format(vl53.distance))
        vl53.clear_interrupt()
        time.sleep(0.5)   # Delay 0.5 second
