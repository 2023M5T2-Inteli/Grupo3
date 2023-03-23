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


def test_hx711():
    print("Conectando ao módulo de peso")
    Time.sleep(1000)
    # Create a new HX711 object with the specified pin numbers
    pin_OUT = Pin("D12", Pin.IN, pull=Pin.PULL_DOWN)
    pin_SCK = Pin("D13", Pin.OUT)

    spi = SPI(mode=SPI, baudrate=1000000, polarity=0,phase=0, pins=(None, pin_SCK, pin_OUT))

    hx711 = HX711(pin_SCK, pin_OUT, spi)
    hx711.tare()

   # Loop until the program is interrupted
    while True:
        try:
            value = hx711.read()
            value = hx711.get_value()
            # Read the weight from the sensor and display it
            print(str(value))
        except:
            # If there's an error reading the sensor, display a message
            print("Erro: módulo de peso não encontrado")
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
        Dobot.move_to(-53, 220, 0, 0)
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
    Dobot.move_to(-0,  -247,  150, 0)
    # Wait 500ms
    Time.sleep(500)
    # Move the arm to position B
    Dobot.move_to(-0,  -247,  -65, 0)


def scanFirstTray():
    # Initialize a counter variable.
    repeat = 0
    # Turn on an electromagnet.
    turnOnElectromagnet()
    # Loop 10 times.
    while repeat != 10:
        # If the counter is even, move to a certain position.
        if (repeat % 2 == 0):
            Dobot.move_to(-0,  -247,  -65, 0)
        # Otherwise, move to a different position.
        else:
            Dobot.move_to(-21,  -340,  -65, 0)
        # Increment the counter.
        repeat = repeat + 1


def iniSecondTray():
    # Display a message on a display.
    Display.print("Separando na segunda bandeja!")
    # Move the arm to a certain position.
    Dobot.move_to(246,  -2,  100, 0)
    # Wait for a period of time.
    Time.sleep(500)
    # Move the arm to a different position.
    Dobot.move_to(246,  -2,  -66, 0)
    # Wait for a period of time.
    Time.sleep(500)


def scanSecondTray():
    # Initialize a counter variable.
    repeat = 0
    # Loop 6 times.
    while repeat != 6:
        # If the counter is even, move to a certain position.
        if (repeat % 2 == 0):
            Dobot.move_to(246,  -2,  -66, 0)
        # Otherwise, move to a different position.
        else:
            Dobot.move_to(342,  -16,  -66, 0)
        # Increment the counter.
        repeat = repeat + 1


def iniThirdTray():
    # Display a message on a display.
    Display.print("Separando na terceira bandeja!")
    # Move the arm to a certain position.
    Dobot.move_to(2,  220,  100, 0)
    # Wait for a period of time.
    Time.sleep(500)
    # Move the arm to a different position.
    Dobot.move_to(2,  220,  -65, 0)
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
            Dobot.move_to(2,  220,  -65, 0)
        # Otherwise, move to a different position.
        else:
            Dobot.move_to(2,  320,  -65, 0)
        # Increment the counter.
        repeat = repeat + 1


def upArm():
    # Get the current position of the arm.
    [x, y, z, r] = Dobot.get_pose()[0:4]
    # Wait for a period of time.
    Time.sleep(1000)
    # Move the arm up to a certain position.
    Dobot.move_to(x, y,  100, 0)


def finish():
    Dobot.set_home()  # Set Dobot to its home position
    Time.sleep(500)  # Wait for 500 milliseconds
    Display.print("Ensaio finalizado!")  # Print "Ensaio finalizado!" message to the display

def set_magnetic_field():
    is_confirm = False
    magnetic_field = 0
    while(is_confirm == False):
        print("Campo: ", magnetic_field)
        if Keyboard.UP.is_pressed() and magnetic_field <12:
            Time.sleep(1000)
            magnetic_field = magnetic_field + 1
            print(str(magnetic_field))

        if Keyboard.DOWN.is_pressed() and magnetic_field >0:
            Time.sleep(1000)
            magnetic_field = magnetic_field - 1
            
            print(str(magnetic_field))
            
        if Keyboard.RIGHT.is_pressed():
            print("Campo escolhido!")
            Time.sleep(2000)
            is_confirm = True
    return magnetic_field



def main():
    test_hx711()
    # magnetic_field = set_magnetic_field()
    # Buzzer.play(200)
    # Time.sleep(150)
    # Buzzer.play(200)
    # while True:
    #     print("Iniciando ensaio")
    # Dobot.setup()  # Set up Dobot
    # isScan = 0  # Initialize isScan variable to 0
    # # Run the loop until isScan is equal to 3
    # while (isScan != 3):
    #     upArm()  # Move the arm up
    #     Dobot.set_home()  # Set Dobot to its home position
    #     iniFirstTray()  # Initialize the first tray
    #     scanFirstTray()  # Scan the first tray
    #     upArm()  # Move the arm up again

    #     iniSecondTray()  # Initialize the second tray
    #     scanSecondTray()  # Scan the second tray

    #     upArm()  # Move the arm up again

    #     iniThirdTray()  # Initialize the third tray
    #     shakeThirdTray()  # Shake the third tray
    #     isScan = isScan + 1  # Increment the isScan variable by 1
    # finish()  # Call the finish function to set Dobot to its home position, wait, and print a message.
