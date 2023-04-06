import dType
from modules import *
from base.api import *
from components import HX711
from machine import Pin, SPI

def test_list_props(item):
    properties_of_dType = dir(item)
    for property_of_dType in properties_of_dType:
        dType.PrintInfo(0, property_of_dType)
        dType.dSleep(750)

def init_hx711():
    pin_OUT = Pin("D12", Pin.IN, pull=Pin.PULL_DOWN)
    pin_SCK = Pin("D13", Pin.OUT)
    spi_SCK = Pin("D13")
    print("Conectando ao modulo de peso")
    Time.sleep(1000)
    spi = SPI(baudrate=1000000, polarity=0, phase=0, sck=spi_SCK, mosi=pin_SCK, miso=pin_OUT)
    hx711 = HX711(pin_SCK, pin_OUT, spi)

    while True:
        try:
            hx711.tare()
            hx711.read()
            value = hx711.get_value()
            print(str(value))       
        except:
            print("Erro: modulo de peso nao encontrado")
        Time.sleep(500)


def turnOnElectromagnet(mf):
    MagicBox.IO.set_pin_mode(12, magicbox.DO)
    Time.sleep(500)
    MagicBox.IO.set_pin_value(12, 1)
    Time.sleep(500)

def turnOffElectromagnet():
    MagicBox.IO.set_pin_mode(12, magicbox.DO)
    Time.sleep(500)
    MagicBox.IO.set_pin_value(12, 0)

def showPosition():
    position = Dobot.get_pose()
    positionStr = "X {0} Y:{1} Z:{2}".format(position[0], position[1], position[2])
    print(positionStr)

def iniFirstTray():
    Display.print("Scanneando primeira bandeja!")
    Time.sleep(500)
    Dobot.move_to(-210,  275,  10, 0,1)
    
def scanFirstTray():
    #turnOnElectromagnet()
    Coordinates = [
        [342,  52,  10, 0, 1], 
        [310,  51,  10, 0, 1], 
        [-185,  254,  10, 0, 1],   
        [-158,  217,  10, 0, 1],
        [266,  41,  10, 0, 1]]
    for i in range(0,5):
        Dobot.move_to(Coordinates[i][0],Coordinates[i][1],Coordinates[i][2],Coordinates[i][3],Coordinates[i][4])
        Time.sleep(1000)   


def iniSecondTray():
    Display.print("Separando na segunda bandeja!")
    Dobot.move_to(340,  -63,  76, 0, 1)
    Time.sleep(500)
    Dobot.move_to(340,  -63,  16, 0, 1)

def scanSecondTray():
    Coordinates = [
        [25,  -349,  10, 0, 1], 
        [22,  -310,  10, 0, 1], 
        [308,  -46,  10, 0, 1],
        [264,  -46,  10, 0, 1],
        [26,  -267,  10, 0, 1]]
    for i in range(0,5):
        Dobot.move_to(Coordinates[i][0],Coordinates[i][1],Coordinates[i][2],Coordinates[i][3],Coordinates[i][4])
        Time.sleep(1000)   


def iniThirdTray():
    Display.print("Separando na terceira bandeja!")
    Dobot.move_to(-67,  -304,  125, 0,1)
    Time.sleep(500)
    Dobot.move_to(-71,  -301,  10, 0,1)
    Time.sleep(100)
    


def shakeThirdTray():
    repeat = 0
    turnOffElectromagnet()
    while repeat != 6:
        # If the counter is even, move to a certain position.
        if (repeat % 2 == 0):
            Dobot.move_to(-71,  -301,  10, 0,1)
        # Otherwise, move to a different position.
        else:
            Dobot.move_to(-211,  -230,  10, 0,1)
        # Increment the counter.
        repeat = repeat + 1


def upArm():
    position = Dobot.get_pose()
    x = position['x']
    y = position['y']
    Time.sleep(1000)
    Dobot.move_to(x, y,  150, 0)


def finish():   
    upArm()
    Dobot.set_home()
    Time.sleep(500)
    Display.print("Ensaio finalizado!")
    play_buzzer()

def set_magnetic_field():
    is_confirm = False
    magnetic_field = 50
    while(is_confirm == False):
        print("Campo: ", magnetic_field)
        if Keyboard.UP.is_pressed() and magnetic_field <100:
            Time.sleep(1000)
            magnetic_field = magnetic_field + 10
            print(str(magnetic_field))

        if Keyboard.DOWN.is_pressed() and magnetic_field >10:
            Time.sleep(1000)
            magnetic_field = magnetic_field - 10
            print(str(magnetic_field))

        if Keyboard.RIGHT.is_pressed():
            print("Campo escolhido!")
            Time.sleep(2000)
            is_confirm = True
    return magnetic_field

def play_buzzer():
    Buzzer.play(200)
    Time.sleep(150)
    Buzzer.play(200)

def main():
    magnetic_field = set_magnetic_field()
    play_buzzer()
    while True:
        print("Iniciando ensaio") 
        isScan = 0
        while (isScan != 2):
            
            upArm() 
            Dobot.set_home()
            turnOnElectromagnet(magnetic_field)
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
        Time.sleep(2000)
        #init_hx711()
