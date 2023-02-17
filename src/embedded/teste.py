from machine import Pin
from time import sleep

pin = Pin("LED", Pin.OUT)f5

while True:
    pin.toggle()
    sleep(1)