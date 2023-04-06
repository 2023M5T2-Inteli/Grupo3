# Import necessary modules
import sys
sys.path.append('Script')  # Add the path to the script folder
import dType
from modules import *
from base.api import *
from components import HX711
from machine import Pin, SPI

# Set pin 12 to output mode
MagicBox.IO.set_pin_mode(13, magicbox.PWM)
MagicBox.IO.set_pin_mode(12, magicbox.DO)
MagicBox.IO.set_pin_value(12, 1)
Time.sleep(500) # Wait 500ms

while(True):
    MagicBox.IO.set_pin_pwm(13,5000, 100)
    Time.sleep(5000)
    MagicBox.IO.set_pin_pwm(13,5000, 75)
    Time.sleep(5000)
    MagicBox.IO.set_pin_pwm(13,5000, 50)
    Time.sleep(5000)
    MagicBox.IO.set_pin_pwm(13,5000, 25)
    Time.sleep(5000)
    MagicBox.IO.set_pin_pwm(13,5000, 0)