import dType
import time


class Time:
    @staticmethod
    def sleep(ms: int) -> None:
        dType.dSleep(ms)

    @staticmethod
    def get_millis() -> int:
        return time.time()
