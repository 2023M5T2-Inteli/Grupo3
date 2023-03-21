import pyb
import machine
from modules import Time


class BuzzerPinMapping:
    BUZZER = 'E10'


class Buzzer:
    __PIN = machine.Pin(BuzzerPinMapping.BUZZER)

    @staticmethod
    def play(duration: int = 128) -> None:
        Buzzer.__PIN.on()
        time.sleep_ms(duration)
        Buzzer.__PIN.off()

    @staticmethod
    def turn_off() -> None:
        Buzzer.__PIN.off()
