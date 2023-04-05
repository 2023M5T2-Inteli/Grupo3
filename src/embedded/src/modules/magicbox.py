from base.api import *  # import necessary modules from base package

class MagicBox:  # create a class named MagicBox
    @staticmethod
    def restart() -> None:  # create a static method named restart that returns None
        dType.RestartMagicBox(0)  # restart the magicbox

    class HBridge:  # create a nested class named HBridge
        @staticmethod
        def set_external_motor(index: int, enable: bool, speed: int) -> None:  # create a static method named set_external_motor that returns None
            '''
            index: the motor index
            enable: whether to enable the motor
            speed: the speed of the motor
            '''
            magicbox.set_emotor(index, enable, speed)  # set the external motor using the given index, enable and speed values

    class IO:  # create another nested class named IO
        @staticmethod
        def set_pin_mode(pin: int, mode: int) -> None:  # create a static method named set_pin_mode that returns None
            '''
            pin: the EIO number
            mode: the pin mode:
                magicbox.DUMMY
                magicbox.DI
                magicbox.DO
                magicbox.ADC
                magicbox.PWM
            '''
            magicbox.set_port(pin, mode)  # set the pin mode using the given pin number and mode value

        @staticmethod
        def set_pin_value(pin: int, value: int) -> None:  # create a static method named set_pin_value that returns None
            '''
            pin: the EIO number
            value: the value to set the pin to
            '''
            magicbox.set_io(pin, value)  # set the pin value using the given pin number and value

        @staticmethod
        def read_in_pin_value(pin: int) -> int:  # create a static method named read_in_pin_value that returns an integer
            '''
            pin: the EIO number
            '''
            return magicbox.get_di(pin)["level"]  # return the level of the input pin using the given pin number

        @staticmethod
        def read_out_pin_value(pin: int) -> int:  # create a static method named read_out_pin_value that returns an integer
            '''
            pin: the EIO number
            '''
            return magicbox.get_do(pin)["level"]  # return the level of the output pin using the given pin number

        @staticmethod
        def set_pin_pwm(pin: int, frequency: int, duty_cycle: int) -> None:  # create a static method named set_pin_pwm that returns None
            '''
            pin: the EIO number
            frequency: the frequency of the PWM signal
            duty_cycle: the duty cycle of the PWM signal
            '''
            magicbox.set_pwm(pin, frequency, duty_cycle)  # set the PWM signal using the given pin number, frequency and duty cycle values

        @staticmethod
        def get_pin_adc(pin: int) -> int:  # create a static method named get_pin_adc that returns an integer
            '''
            pin: the EIO number
            '''
            return magicbox.get_ad(pin)["level"]  # return the level of the ADC pin using the given pin number
