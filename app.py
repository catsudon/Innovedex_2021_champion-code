import sys, csv
from time import sleep
import pyfirmata

port = "COM3"
board = pyfirmata.Arduino(port)

it = pyfirmata.util.Iterator(board)
it.start()

base = board.get_pin('d:8:s')
left_sholder = board.get_pin('d:9:s')
right_sholder = board.get_pin('d:10:s')
glipper = board.get_pin('d:11:s')
##for i in range(50):
##    pin8.write(i)
##    sleep(0.1)


# base 5-175 ขวา-ซ้าย
# sholderซ้าย 50ต่ำ 120สูง
# sholderขวา 90-150 ชักเข้าออก
# glipper 80degกาง 180=หุบ