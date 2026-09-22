# What it does: Draws pixels, lines, rectangles, circles and text on a 128x64 I2C OLED display
# Wiring:       Connect the OLED module to I2C1 (SCL1/SDA1), module address 0x3C
# Expected output: The OLED shows the drawn graphics and "Hello WalnutPi!", then "Done!" is printed
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/gpio/i2c_oled

import board
import busio
import adafruit_ssd1306

# Construct the I2C object
i2c = busio.I2C(board.SCL1, board.SDA1)

# Construct the OLED object, the matching OLED module address is 0x3C
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)

# Clear the screen
display.fill(0)
display.show()

# Draw a pixel (x, y, color)
display.pixel(5, 5, 1)

# Draw a horizontal line (x, y, width, color)
display.hline(5, 10, 20, 1)

# Draw a rectangle (x, y, width, height, color)
display.rect(5, 15, 20, 10, 1)

# Draw a circle (x, y, radius, color)
display.circle(50, 15, 10, 1)

# Draw text (string, x, y, color, font)
display.text("Hello WalnutPi!", 5, 40, 1, font_name='font5x8.bin')

# Update the display
display.show()

print('Done!')
