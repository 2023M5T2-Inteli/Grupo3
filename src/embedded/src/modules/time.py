# Importing everything from the 'api' module within the 'base' package
from base.api import *

# Defining a 'Time' class
class Time:

    # A static method 'sleep' that takes an integer argument 'ms' and returns nothing (None)
    # It calls a function 'dSleep' from the imported 'dType' module with the 'ms' argument
    @staticmethod
    def sleep(ms: int) -> None:
        dType.dSleep(ms)

    # A static method 'get_millis' that takes no arguments and returns an integer value
    # It returns the current time in milliseconds using the 'time' module's 'time()' function
    @staticmethod
    def get_millis() -> int:
        return time.time()
