import dType


class PinMode:
    IOFunctionDummy = 0
    IOFunctionDO = 1
    IOFunctionPWM = 2
    IOFunctionDI = 3
    IOFunctionADC = 4


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
            dType.SetEMotorExtEx(0, index, enable, speed, 0)

    class IO:
        @staticmethod
        def set_pin_mode(pin: int, mode: int) -> None:
            '''
            pin: the EIO number
            mode: the pin mode ( PinMode enum )
            '''
            dType.SetIOMultiplexingExtEx(0, pin, mode, 0)

        @staticmethod
        def set_pin_value(pin: int, value: int) -> None:
            '''
            pin: the EIO number
            value: the value to set the pin to
            '''
            dType.SetIODOExtEx(0, pin, value, 1)

        @staticmethod
        def read_pin_value(pin: int) -> int:
            '''
            pin: the EIO number
            '''
            return dType.GetIODIExt(0, pin)[0]

        @staticmethod
        def set_pin_pwm(pin: int, frequency: int, duty_cycle: int) -> None:
            '''
            pin: the EIO number
            frequency: the frequency of the PWM signal
            duty_cycle: the duty cycle of the PWM signal
            '''
            dType.SetIOPWMExtEx(0, pin, frequency, duty_cycle, 1)

        @staticmethod
        def get_pin_pwm(pin: int) -> int:
            '''
            pin: the EIO number
            '''
            return dType.GetIOPWMExt(0, pin)

        @staticmethod
        def get_pin_adc(pin: int) -> int:
            '''
            pin: the EIO number
            '''
            return dType.GetIOADCExt(0, pin)
