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


def turnOnElectromagnet():
    MagicBox.IO.set_pin_mode(12, PinMode.IOFunctionDO)
    Time.sleep(500)
    MagicBox.IO.set_pin_value(12, 1)
    Time.sleep(500)


def turnOffElectromagnet():
    MagicBox.IO.set_pin_mode(12, PinMode.IOFunctionDO)
    Time.sleep(500)
    MagicBox.IO.set_pin_value(12, 0)
    Time.sleep(500)


def showPosition():
    position = Dobot.get_pose()
    positionStr = "X {0} Y:{1} Z:{2}".format(position[0], position[1], position[2])
    Display.print(positionStr)



def iniFirstTray():
    Display.print("Scanneando primeira bandeja!")
    Dobot.move_to(0,  -220,  0, 0)
    Time.sleep(1000)
    Dobot.move_to(-53,  -220,  -67, 0)
    Time.sleep(1000)


def scanFirstTray():
    repeat = 1
    MoveZ = -53
    turnOnElectromagnet()
    while repeat != 10:
        if (repeat % 2 == 0):
            moveX = -220
        else:
            moveX = -340     
        Dobot.move_to(MoveZ,  moveX,  -67, 0)
        Time.sleep(1500)
        MoveZ = MoveZ +10
        repeat = repeat + 1

def iniSecondTray():
    Display.print("Separando na segunda bandeja!")
    Dobot.move_to(0,  100,  10, 0)
    Time.sleep(1000)
    # Dobot.move_to(-53,  -220,  -67, 0)
    # Time.sleep(1000)


def upArm():
    [x,y,z,r] = Dobot.get_pose()[0:4]
    Dobot.move_to(x, y,  0, 0)


def main():
    Dobot.setup()
    upArm()
    Dobot.set_home()
    Time.sleep(2000)
    iniFirstTray()
    scanFirstTray()
    upArm()
    Dobot.set_home()
    showPosition
    

