from base.api import *


class Display:
    @staticmethod
    def print(text: str) -> None:
        magicbox.set_oled_text(1, text)

    @staticmethod
    def print_on_position(x: int, y: int, text: str) -> None:
        magicbox.set_oled_pos_text(1, x, y, text)

    @staticmethod
    def clear() -> None:
        magicbox.set_oled_clear(1)

    @staticmethod
    def set_progress_bar(progress: int) -> None:
        dType.SetProgbar(0, int(progress))
