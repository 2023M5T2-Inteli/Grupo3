# Import the base API module
from base.api import *

# Define a class called TTSCMD
class TTSCMD:
    # Define constants for commands
    STOP = 0
    SUSPEND = 1
    RESUME = 2
    NEXT = 3
    PREVIOUS = 4

# Define a class called Sound
class Sound:
    # Define a static method to play an effect
    @staticmethod
    def play_effect(index: int) -> None:
        # Set the TTS effect using the magicbox API
        magicbox.set_tts_effect(port=2, index=index)

    # Define a static method to play music
    @staticmethod
    def play_music(index: int) -> None:
        # Set the TTS music using the magicbox API
        magicbox.set_tts_music(port=2, index=index)

    # Define a static method to play a tone
    @staticmethod
    def play_tone(index: int) -> None:
        # Set the TTS tone using the magicbox API
        magicbox.set_tts_tone(port=2, index=index)

    # Define a static method to set the volume
    @staticmethod
    def set_volume(volume: int) -> None:
        # Set the TTS volume using the magicbox API
        magicbox.set_tts_volume(port=2, sound=volume)

    # Define a static method to stop the TTS
    @staticmethod
    def stop() -> None:
        # Send the stop command to the TTS using the magicbox API
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.STOP)

    # Define a static method to suspend the TTS
    @staticmethod
    def suspend() -> None:
        # Send the suspend command to the TTS using the magicbox API
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.SUSPEND)

    # Define a static method to resume the TTS
    @staticmethod
    def resume() -> None:
        # Send the resume command to the TTS using the magicbox API
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.RESUME)

    # Define a static method to go to the next TTS message
    @staticmethod
    def next() -> None:
        # Send the next command to the TTS using the magicbox API
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.NEXT)

    # Define a static method to go to the previous TTS message
    @staticmethod
    def previous() -> None:
        # Send the previous command to the TTS using the magicbox API
        magicbox.set_tts_cmd(port=2, cmd=TTSCMD.PREVIOUS)
