import sys

sys.path.append('Script')  # Add the path to the script folder

if __name__ == '__main__':
    from modules import *

    from base.api import *
    import modules.controller as Controller

    while True:
        magicbox.set_tts_tone(port=2, index=1)
        Time.sleep(100)
        Controller.main()
