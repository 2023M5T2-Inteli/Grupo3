# Import necessary modules
import pyb
import machine
from modules import Time

# Define a class to map button pins
class ButtonsPinMaping:
    UP = 'E3'
    DOWN = 'C13'
    LEFT = 'C15'
    RIGHT = 'C14'
    CENTER = 'D4'

# Define a class to represent a single button
class Button:
    __pin = None

    # Initialize the button with a pin
    def __init__(self, pin_port: str) -> None:
        self.__pin = machine.Pin(pin_port)

    # Check if the button is currently pressed
    def is_pressed(self) -> bool:
        return self.__pin.value() == 0

    # Check if the button is currently released
    def is_released(self) -> bool:
        return self.__pin.value() == 1

    # Wait for the button to be pressed
    def wait_for_press(self) -> None:
        while self.is_released():
            pass

    # Wait for the button to be released
    def wait_for_release(self) -> None:
        while self.is_pressed():
            pass

    # Check if the button is being held down for a certain amount of time
    def is_held(self, delay: int = 1250) -> bool:
        start_time = Time.get_millis()
        while self.is_pressed():
            if Time.get_millis() - start_time >= delay:
                return True
        return False

    # Wait for the button to be held down for a certain amount of time
    def wait_for_held(self, delay: int = 1250) -> None:
        while not self.is_held(delay):
            pass

# Define a class to represent a keyboard with multiple buttons
class Keyboard:
    # Initialize buttons for each direction and center
    UP = Button(ButtonsPinMaping.UP)
    DOWN = Button(ButtonsPinMaping.DOWN)
    LEFT = Button(ButtonsPinMaping.LEFT)
    RIGHT = Button(ButtonsPinMaping.RIGHT)
    CENTER = Button(ButtonsPinMaping.CENTER)
