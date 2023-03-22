from base.api import *


class MagicBox:
    @staticmethod
    def restart() -> None:
        dType.RestartMagicBox(0)

    class HBridge:
        @staticmethod
        def set_external_motor(index: int, enable: bool, speed: int) -> None:
            '''
            index: the motor index
            enable: whether to enable the motor
            speed: the speed of the motor
            '''
            magicbox.set_emotor(index, enable, speed)

    class IO:
        @staticmethod
        def set_pin_mode(pin: int, mode: int) -> None:
            '''
            pin: the EIO number
            mode: the pin mode:
                magicbox.DUMMY
                magicbox.DI
                magicbox.DO
                magicbox.ADC
                magicbox.PWM
            '''
            magicbox.set_port(pin, mode)

        @staticmethod
        def set_pin_value(pin: int, value: int) -> None:
            '''
            pin: the EIO number
            value: the value to set the pin to
            '''
            magicbox.set_io(pin, value)

        @staticmethod
        def read_in_pin_value(pin: int) -> int:
            '''
            pin: the EIO number
            '''
            return magicbox.get_di(pin)["level"]

        @staticmethod
        def read_out_pin_value(pin: int) -> int:
            '''
            pin: the EIO number
            '''
            return magicbox.get_do(pin)["level"]

        @staticmethod
        def set_pin_pwm(pin: int, frequency: int, duty_cycle: int) -> None:
            '''
            pin: the EIO number
            frequency: the frequency of the PWM signal
            duty_cycle: the duty cycle of the PWM signal
            '''
            magicbox.set_pwm(pin, frequency, duty_cycle)

        @staticmethod
        def get_pin_adc(pin: int) -> int:
            '''
            pin: the EIO number
            '''
            return magicbox.get_ad(pin)["level"]
