# Importing required modules
import pyb
import machine
from modules import Time

# Defining a class for BuzzerPinMapping
class BuzzerPinMapping:
    # Defining the pin for the buzzer
    BUZZER = 'E10'

# Defining a class for the Buzzer
class Buzzer:
    # Setting the pin for the buzzer
    __PIN = machine.Pin(BuzzerPinMapping.BUZZER)

    # Method to play the buzzer sound with a given duration (in ms)
    @staticmethod
    def play(duration: int = 128) -> None:
        # Turn on the buzzer
        Buzzer.__PIN.on()
        # Wait for the specified duration
        Time.sleep(duration)
        # Turn off the buzzer
        Buzzer.__PIN.off()

    # Method to turn off the buzzer
    @staticmethod
    def turn_off() -> None:
        # Turn off the buzzer
        Buzzer.__PIN.off()
