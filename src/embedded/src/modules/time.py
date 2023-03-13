from base.api import *


class Time:
    @staticmethod
    def sleep(ms: int) -> None:
        dType.dSleep(ms)
