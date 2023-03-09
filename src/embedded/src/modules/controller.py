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

def shakeAfterTurnOff():
    i = 0
    while i < 4:
        Dobot.move_to(-53, 220, 20, 0)
        Dobot.move_to(-53, 220, 0, 0)
        i += 1 


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
    repeat = 0
    MoveX = -53
    turnOnElectromagnet()
    while repeat != 10:
        if (repeat % 2 == 0):
            moveY = -220
        else:
            moveY = -340     
        Dobot.move_to(MoveX,  moveY,  -67, 0)
        Time.sleep(1500)
        MoveX = MoveX +10
        repeat = repeat + 1

def iniSecondTray():
    Display.print("Separando na segunda bandeja!")
    Dobot.move_to(248,  -4,  -48, 0)
    Time.sleep(1000)
    # Dobot.move_to(-53,  -220,  -67, 0)
    # Time.sleep(1000)

def shakeSecondTray():
    repeat2 = 1
    MoveX = 248
    while repeat2 != 10:
        if (repeat2 % 2 == 0):
            moveY = -60
        else:
            moveY = -4    
        Dobot.move_to(MoveX,  moveY,  -48, 0)
        Time.sleep(1500)
        MoveX = MoveX -10
        repeat2 = repeat2 + 1

def thirdTray():
    
    Display.print("Separando na terceira bandeja!")
    Dobot.move_to(-53, 220, 0, 0)
    Dobot.move_to(-53, 220, -65, 0)
    turnOffElectromagnet()
    Dobot.move_to(-53, 300, -65, 0)
    Dobot.move_to(-53, 220, -65, 0)
    upArm()
    
    

def upArm():
    [x,y,z,r] = Dobot.get_pose()[0:4]
    Dobot.move_to(x, y,  0, 0)

def finish():
    Dobot.set_home()
    Dobot.move_to(162, -8, 39, 0)
    Time.sleep(500)
    Display.print("Ensaio finalizado!")

def main():
    Dobot.setup()
    showPosition()
    upArm()
    iniSecondTray()
    shakeSecondTray()
    # upArm()
    # Dobot.set_home()
    # Time.sleep(2000)
    # iniFirstTray()
    # scanFirstTray()
    # upArm()
    # Dobot.set_home()
    # showPosition()
    thirdTray()
    shakeAfterTurnOff()

