import pyb
import machine
from modules import Time


class BuzzerPinMapping:
    BUZZER = 'E10'


class Notes:
    C6 = 1047
    CS6 = 1109
    D6 = 1175
    DS6 = 1245
    E6 = 1319
    F6 = 1397
    FS6 = 1480
    G6 = 1568
    GS6 = 1661
    A6 = 1760
    AS6 = 1865
    B6 = 1976
    C7 = 2093
    CS7 = 2217
    D7 = 2349
    DS7 = 2489
    E7 = 2637
    F7 = 2794
    FS7 = 2960
    G7 = 3136
    GS7 = 3322
    A7 = 3520
    AS7 = 3729
    B7 = 3951


class Buzzer:
    __PIN = machine.Pin(BuzzerPinMapping.BUZZER)

    def play(duration: int = 128) -> None:
        Buzzer.__PIN.on()
        Time.sleep(duration)
        Buzzer.__PIN.off()

    def play_tone(notes: list[Notes], delay: int = 128, active_duty: int = 1000) -> None:
        buzzer_pwm = machine.PWM(Buzzer.__PIN)
        for note in notes:
            if note == 0 or note is None:
                buzzer_pwm.duty(0)
            else:
                buzzer_pwm.freq(note)
                buzzer_pwm.duty_u16(active_duty)
            Time.sleep(delay)
        buzzer_pwm.duty_u16(0)
        buzzer_pwm.deinit()

    def turn_off() -> None:
        Buzzer.__PIN.off()

    def play_test_mario(self) -> None:
        Buzzer.__PIN.play_tone([Notes.E7, Notes.E7, 0, Notes.E7, 0, Notes.C7, Notes.E7, 0, Notes.G7, 0, 0, 0, Notes.G6, 0, 0, 0, Notes.C7, 0, 0, Notes.G6, 0, 0, Notes.E6, 0, 0, Notes.A6, 0, Notes.B6, 0, Notes.AS6, Notes.A6, 0, Notes.G6, Notes.E7, Notes.G7, Notes.A7, 0, Notes.F7, Notes.G7,
                                0, Notes.E7, 0, Notes.C7, Notes.D7, Notes.B6, 0, 0, Notes.C7, 0, 0, Notes.G6, 0, 0, Notes.E6, 0, 0, Notes.A6, 0, Notes.B6, 0, Notes.AS6, Notes.A6, 0, Notes.G6, Notes.E7, Notes.G7, Notes.A7, 0, Notes.F7, Notes.G7, 0, Notes.E7, 0, Notes.C7, Notes.D7, Notes.B6, 0, 0])
