from base.api import *


class TTSCMD:
    STOP = 0
    SUSPEND = 1
    RESUME = 2
    NEXT = 3
    PREVIOUS = 4


class Sound:
    @staticmethod
    def play_effect(index: int) -> None:
        magicbox.set_tts_effect(port=2, index=index)

    @staticmethod
    def play_music(index: int) -> None:
        magicbox.set_tts_music(port=2, index=index)

    @staticmethod
    def play_tone(index: int) -> None:
        magicbox.set_tts_tone(port=2, index=index)

    @staticmethod
    def set_volume(volume: int) -> None:
        magicbox.set_tts_volume(port=2, sound=volume)

    @staticmethod
    def stop() -> None:
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.STOP)

    @staticmethod
    def suspend() -> None:
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.SUSPEND)

    @staticmethod
    def resume() -> None:
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.RESUME)

    @staticmethod
    def next() -> None:
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.NEXT)

    @staticmethod
    def previous() -> None:
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.PREVIOUS)
