# Importing required modules from base.api
from base.api import *

# Defining a class for Display
class Display:
    # Method to print the given text on OLED screen
    @staticmethod
    def print(text: str) -> None:
        # Setting the OLED text on the first page of OLED
        magicbox.set_oled_text(1, text)

    # Method to print the given text on a specific position on OLED screen
    @staticmethod
    def print_on_position(x: int, y: int, text: str) -> None:
        # Setting the OLED text on the given (x, y) position of the first page of OLED
        magicbox.set_oled_pos_text(1, x, y, text)

    # Method to clear the OLED screen
    @staticmethod
    def clear() -> None:
        # Clearing the first page of OLED
        magicbox.set_oled_clear(1)

    # Method to set the progress bar on OLED screen
    @staticmethod
    def set_progress_bar(progress: int) -> None:
        # Setting the progress bar on OLED screen with the given progress percentage
        dType.SetProgbar(0, int(progress))
