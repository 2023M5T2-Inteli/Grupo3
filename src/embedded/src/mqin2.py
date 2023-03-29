# Import necessary modules
import sys

sys.path.append('Script')  # Add the path to the script folder
import dType
from modules import *
# from components import *
from base.api import *
from components import HX711
from machine import Pin, SPI


    # Set pin 12 to output mode
MagicBox.IO.set_pin_mode(12, magicbox.PWM)
    # Wait 500ms
Time.sleep(500)
    # Set pin 12 to high
MagicBox.IO.set_pin_value(12, 1)
    # Wait 500ms
Time.sleep(5000)
MagicBox.IO.set_pin_value(12, 0)
Time.sleep(5000)
MagicBox.IO.set_pin_value(12, 1)