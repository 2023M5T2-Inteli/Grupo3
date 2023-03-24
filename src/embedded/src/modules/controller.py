# Import necessary modules
import dType
from modules import *
# from components import *
from base.api import *
from components import HX711
from machine import Pin, SPI


# Function to test the properties of a dType object


def test_list_props(item):
    # Get list of properties of the object
    properties_of_dType = dir(item)

    # Iterate over the properties and print them out
    for property_of_dType in properties_of_dType:
        dType.PrintInfo(0, property_of_dType)
        dType.dSleep(750)

# Function to test the HX711 sensor


def init_hx711():
    # Create a new HX711 object with the specified pin numbers
    pin_OUT = Pin("D12", Pin.IN, pull=Pin.PULL_DOWN)
    pin_SCK = Pin("D13", Pin.OUT)
    spi_SCK = Pin("D13")
    print("Conectando ao modulo de peso")
    Time.sleep(1000)
    spi = SPI(baudrate=1000000, polarity=0,
          phase=0, sck=spi_SCK, mosi=pin_SCK, miso=pin_OUT)

    hx711 = HX711(pin_SCK, pin_OUT, spi)
    

   # Loop until the program is interrupted
    while True:
        try:
            hx711.tare()
            hx711.read()
            value = hx711.get_value()
            # Read the weight from the sensor and display it
            print(str(value))
        except:
            # If there's an error reading the sensor, display a message
            print("Erro: modulo de peso não encontrado")
        # Wait 500ms before trying to read the sensor again
        Time.sleep(500)


# Function to turn on the electromagnet


def turnOnElectromagnet():
    # Set pin 12 to output mode
    MagicBox.IO.set_pin_mode(12, magicbox.DO)
    # Wait 500ms
    Time.sleep(500)
    # Set pin 12 to high
    MagicBox.IO.set_pin_value(12, 1)
    # Wait 500ms
    Time.sleep(500)

# Function to turn off the electromagnet


def turnOffElectromagnet():
    # Set pin 12 to output mode
    MagicBox.IO.set_pin_mode(12, magicbox.DO)
    # Wait 500ms
    Time.sleep(500)
    # Set pin 12 to low
    MagicBox.IO.set_pin_value(12, 0)
    # Wait 500ms
    Time.sleep(500)

# Function to shake the arm after turning off the electromagnet


def shakeAfterTurnOff():
    # Loop 4 times
    i = 0
    while i < 4:
        # Move the arm to position A
        Dobot.move_to(-53, 220, 20, 0)
        # Move the arm to position B
        Dobot.move_to(-53, 220, -1, 0)
        # Increment the counter
        i += 1

# Function to display the current position of the arm


def showPosition():
    # Get the current pose of the arm
    position = Dobot.get_pose()
    # Convert the pose to a string and display it
    positionStr = "X {0} Y:{1} Z:{2}".format(position[0], position[1], position[2])
    Display.print(positionStr)

# Function to initialize the first tray


def iniFirstTray():
    # Display a message
    Display.print("Scanneando primeira bandeja!")
    # Wait 500ms
    Time.sleep(500)
    # Move the arm to position A
    Dobot.move_to(-13,  -235,  150, 0,1)
    # Wait 500ms
    Time.sleep(500)
    # Move the arm to position B
    Dobot.move_to(-13,  -230,  -4, 0,1)


def scanFirstTray():
    # Initialize a counter variable.
    repeat = 0
    # Turn on an electromagnet.
    turnOnElectromagnet()
    # Loop 10 times.
    while repeat != 10:
        # If the counter is even, move to a certain position.
        if (repeat % 2 == 0):
            Dobot.move_to(-13,  -370,  -4, 0, 1)       
        # Otherwise, move to a different position.
        else:
            Dobot.move_to(-13,  -230,  -4, 0, 1)
        # Increment the counter.
        repeat = repeat + 1


def iniSecondTray():
    # Display a message on a display.
    Display.print("Separando na segunda bandeja!")
    # Move the arm to a certain position.
    Dobot.move_to(230,  10,  150, 0, 1)
    # Wait for a period of time.
    Time.sleep(500)
    # Move the arm to a different position.
    Dobot.move_to(243,  13,  -3, 0,1)
    # Wait for a period of time.
    Time.sleep(500)


def scanSecondTray():
    # Initialize a counter variable.
    repeat = 0
    # Loop 6 times.
    while repeat != 6:
        # If the counter is even, move to a certain position.
        if (repeat % 2 == 0):
            Dobot.move_to(360,  13,  -3, 0,1)
            
        # Otherwise, move to a different position.
        else:
            Dobot.move_to(243,  13,  -3, 0,1)
        # Increment the counter.
        repeat = repeat + 1


def iniThirdTray():
    # Display a message on a display.
    Display.print("Separando na terceira bandeja!")
    # Move the arm to a certain position.
    Dobot.move_to(-1,  230,  150, 0,1)
    # Wait for a period of time.
    Time.sleep(500)
    # Move the arm to a different position.
    Dobot.move_to(9,  223,  -4, 0,1)
    # Wait for a period of time.
    Time.sleep(100)
    # Turn off an electromagnet.
    turnOffElectromagnet()


def shakeThirdTray():
    # Initialize a counter variable.
    repeat = 0
    # Loop 6 times.
    while repeat != 6:
        # If the counter is even, move to a certain position.
        if (repeat % 2 == 0):
            Dobot.move_to(9,  360,  -4, 0,1)
        # Otherwise, move to a different position.
        else:
            Dobot.move_to(9,  223,  -1, 0,1)
        # Increment the counter.
        repeat = repeat + 1


def upArm():
    # Get the current position of the arm.
    position = Dobot.get_pose()
    x = position['x']
    y = position['y']
    # Wait for a period of time.
    Time.sleep(1000)
    # Move the arm up to a certain position.
    Dobot.move_to(x, y,  150, 0)


def finish():
    upArm()
    Dobot.set_home()  # Set Dobot to its home position
    Time.sleep(500)  # Wait for 500 milliseconds
    Display.print("Ensaio finalizado!")  # Print "Ensaio finalizado!" message to the display
    play_buzzer()

def set_magnetic_field():
    is_confirm = False
    magnetic_field = 1
    while(is_confirm == False):
        print("Campo: ", magnetic_field)
        if Keyboard.UP.is_pressed() and magnetic_field <12:
            Time.sleep(1000)
            magnetic_field = magnetic_field + 1
            print(str(magnetic_field))

        if Keyboard.DOWN.is_pressed() and magnetic_field >1:
            Time.sleep(1000)
            magnetic_field = magnetic_field - 1
            
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
        isScan = 1  # Initialize isScan variable to 0
     # Run the loop until isScan is equal to 3
        while (isScan != 2):
            upArm()  # Move the arm up
            Dobot.set_home()  # Set Dobot to its home position
            iniFirstTray()  # Initialize the first tray
            scanFirstTray()  # Scan the first tray
            upArm()  # Move the arm up again
            iniSecondTray()  # Initialize the second tray
            scanSecondTray()  # Scan the second tray
            upArm()  # Move the arm up again
            iniThirdTray()  # Initialize the third tray
            shakeThirdTray()  # Shake the third tray
            isScan = isScan + 1  # Increment the isScan variable by 1
        finish()  # Call the finish function to set Dobot to its home position, wait, and print a message.
        Time.sleep(2000)  # Wait for 2000 milliseconds
        init_hx711()
