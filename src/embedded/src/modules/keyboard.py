import pyb
import machine
from modules import Time


class ButtonsPinMaping:
    UP = 'E3'
    DOWN = 'C13'
    LEFT = 'C15'
    RIGHT = 'C14'
    CENTER = 'D4'


class Button:
    __pin = None

    def __init__(self, pin_port: str) -> None:
        self.__pin = machine.Pin(pin_port)

    def is_pressed(self) -> bool:
        return self.__pin.value() == 0

    def is_released(self) -> bool:
        return self.__pin.value() == 1

    def wait_for_press(self) -> None:
        while self.is_released():
            pass

    def wait_for_release(self) -> None:
        while self.is_pressed():
            pass

    def is_held(self, delay: int = 1250) -> bool:
        start_time = Time.get_millis()
        while self.is_pressed():
            if Time.get_millis() - start_time >= delay:
                return True
        return False

    def wait_for_held(self, delay: int = 1250) -> None:
        while not self.is_held(delay):
            pass


class Keyboard:
    UP = Button(ButtonsPinMaping.UP)
    DOWN = Button(ButtonsPinMaping.DOWN)
    LEFT = Button(ButtonsPinMaping.LEFT)
    RIGHT = Button(ButtonsPinMaping.RIGHT)
    CENTER = Button(ButtonsPinMaping.CENTER)
