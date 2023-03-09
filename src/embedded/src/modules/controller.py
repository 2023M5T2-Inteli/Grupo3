import dType
from modules import *
from components import *


def test_list_props(item):
    properties_of_dType = dir(item)

    for property_of_dType in properties_of_dType:
        dType.PrintInfo(0, property_of_dType)
        dType.dSleep(750)


def test_hx711():
    hx711 = HX711(15, 16)
    while True:
        try:
            Display.print(str(hx711.read(True)))
        except:
            Display.print("Waiting for HX711 to be ready")
        Time.sleep(500)


def test_hbridge():
    MagicBox.IO.set_pin_mode(12, PinMode.IOFunctionDO)
    while True:
        MagicBox.IO.set_pin_value(12, 1)
        Time.sleep(2000)
        MagicBox.IO.set_pin_value(12, 0)
        Time.sleep(2000)


def main():
    Dobot.setup()
    Dobot.move_to(339.7292,  -108.1285,  -20, 0)
