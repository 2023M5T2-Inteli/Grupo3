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
    Time.sleep(500)
    Dobot.move_to(-0,  -247,  150, 0)
    Time.sleep(500)
    Dobot.move_to(-0,  -247,  -65, 0)

def scanFirstTray():
    repeat = 0
    turnOnElectromagnet()
    while repeat != 10:
        if (repeat % 2 == 0):
            Dobot.move_to(-0,  -247,  -65, 0)
        else:    
            Dobot.move_to(-21,  -340,  -65, 0)
        repeat = repeat + 1

def iniSecondTray():
    Display.print("Separando na segunda bandeja!")
    Dobot.move_to(246,  -2,  100, 0)
    Time.sleep(500)
    Dobot.move_to(246,  -2,  -66, 0)
    Time.sleep(500)
    
def scanSecondTray():
    repeat = 0
    while repeat != 10:
        if (repeat % 2 == 0):
            Dobot.move_to(246,  -2,  -66, 0)
        else:  
            Dobot.move_to(342,  -16,  -66, 0)
        repeat = repeat + 1

def iniThirdTray():
    Display.print("Separando na terceira bandeja!")
    Dobot.move_to(2,  220,  100, 0)
    Time.sleep(500)
    Dobot.move_to(2,  220,  -65, 0)
    Time.sleep(500)
    
def shakeThirdTray():
    repeat = 0
    while repeat != 10:
        if (repeat % 2 == 0):
            Dobot.move_to(2,  220,  -65, 0)
        else:  
            Dobot.move_to(2,  320,  -65, 0)
        repeat = repeat + 1
        
def upArm():
    [x,y,z,r] = Dobot.get_pose()[0:4]
    Time.sleep(1000)
    Dobot.move_to(x, y,  100, 0)

def finish():
    Dobot.set_home()
    Time.sleep(500)
    Display.print("Ensaio finalizado!")

def main():
    Dobot.setup()
    isScan = 0
    while (isScan !=5):
        upArm()
        Dobot.set_home()
        iniFirstTray()
        scanFirstTray()
        upArm()

        iniSecondTray()
        scanSecondTray()

        upArm()

        iniThirdTray()
        shakeThirdTray()
        isScan = isScan + 1
    finish()

