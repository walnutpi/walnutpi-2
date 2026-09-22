# What it does: Collects system information (CPU temp, CPU usage, RAM, disk, IP) and shows it on an I2C OLED
# Wiring:       Connect the OLED module to I2C1 (SCL1/SDA1), module address 0x3C
# Expected output: The OLED refreshes the system information once per second
# Tested on:    WalnutPi 2B / WalnutPi CM2
# Tutorial:     https://wiki.walnutpi.com/en/docs/walnutpi_2/python/gpio/i2c_oled

import os
import socket
import fcntl
import struct
from time import sleep

import board
import busio
import adafruit_ssd1306

# Construct the I2C object
i2c = busio.I2C(board.SCL1, board.SDA1)

# Construct the OLED object, the matching OLED module address is 0x3C
display = adafruit_ssd1306.SSD1306_I2C(128, 64, i2c, addr=0x3C)


# Read the CPU temperature in Celsius
def getCPUtemperature():
    res = os.popen('cat /sys/class/thermal/thermal_zone0/temp').readline()
    return '%.1f' % (int(res) / 1000)


# Return the CPU usage percentage (%), as a string
def getCPUuse():
    return str(os.popen(r"top -b -n1 | awk '/Cpu\(s\):/ {print $2}'").readline().strip())


# Collect RAM information, unit is kB
# Index 0: total memory
# Index 1: used memory
# Index 2: free memory
def getRAMinfo():
    p = os.popen('free')
    i = 0
    while True:
        i = i + 1
        line = p.readline()
        if i == 2:
            return line.split()[1:4]


# Return the SD card capacity, unit is GB
# Index 0: total capacity
# Index 1: used space
# Index 2: remaining space
# Index 3: usage percentage (%)
def getDiskSpace():
    p = os.popen("df -h /")
    i = 0
    while True:
        i = i + 1
        line = p.readline()
        if i == 2:
            return line.split()[1:5]


# Get the local IP address of a network interface, returned as a string
def getIP(ifname):
    s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

    # Exception handling
    try:
        return socket.inet_ntoa(fcntl.ioctl(
            s.fileno(),
            0x8915,   # SIOCGIFADDR
            struct.pack('256s', ifname[:15].encode('utf-8'))
        )[20:24])

    except OSError:
        return '0.0.0.0'


while True:

    # Collect the CPU temperature
    CPU_temp = getCPUtemperature()
    print(CPU_temp)

    # Collect the CPU usage
    CPU_usage = getCPUuse()

    # RAM information, converted to MB
    RAM_stats = getRAMinfo()
    RAM_total = int(int(RAM_stats[0]) / 1000)
    RAM_used = int(int(RAM_stats[1]) / 1000)
    RAM_perc = str(round((RAM_used / RAM_total * 100), 1)) + '%'

    # SD card capacity information
    DISK_stats = getDiskSpace()
    DISK_total = DISK_stats[0]
    DISK_used = DISK_stats[1]
    DISK_perc = DISK_stats[3]   # Usage percentage

    # Wireless network IP information
    Wlan0_IP = getIP("wlan0")

    # Ethernet IP information
    Eth0_IP = getIP("end1")

    # Clear the display
    display.fill(0)

    # Show the information on the OLED
    display.text('CPU Temp: ' + CPU_temp + ' C', 0, 0, 1, font_name='./font5x8.bin')
    display.text('CPU Used: ' + CPU_usage + ' %', 0, 12, 1, font_name='./font5x8.bin')
    display.text('RAM:' + str(RAM_used) + '/' + str(RAM_total) + 'MB' + ' ' + RAM_perc, 0, 24, 1, font_name='./font5x8.bin')
    display.text('DISK:' + str(DISK_used) + '/' + str(DISK_total) + ' ' + DISK_perc, 0, 38, 1, font_name='./font5x8.bin')

    # Show the IP address
    if Wlan0_IP != '0.0.0.0':
        display.text('wlan0:' + Wlan0_IP, 0, 50, 1, font_name='./font5x8.bin')

    elif Eth0_IP != '0.0.0.0':
        display.text('eth0:' + Eth0_IP, 0, 50, 1, font_name='./font5x8.bin')

    else:
        display.text('IP:0.0.0.0', 0, 50, 1, font_name='./font5x8.bin')

    display.show()

    sleep(1)   # Delay, data update interval
