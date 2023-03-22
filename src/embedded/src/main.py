import sys

sys.path.append('Script')  # Add the path to the script folder

if __name__ == '__main__':
    from modules import *

    from base.api import *
    import modules.controller as Controller
    from modules.magnet import Magnet
    Magnet.setup()

    while True:
        Magnet.on()

    #Controller.main()
