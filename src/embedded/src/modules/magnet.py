from modules import MagicBox
from base.api import *

class Magnet:
    @staticmethod
    def setup():
        MagicBox.IO.set_pin_mode(12, magicbox.DO)

    @staticmethod
    def on(value: int = 100):
        MagicBox.IO.set_pin_pwm(12, 10.2, value)

    @staticmethod
    def off():
        MagicBox.IO.set_pin_pwm(12, 10.2, 0)