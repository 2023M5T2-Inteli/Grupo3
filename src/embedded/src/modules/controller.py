# Importing required modules
import dType  # Importing dType module
from modules import *  # Importing all the modules from the modules directory
from base.api import *  # Importing all the modules from the base/api directory
from components import HX711  # Importing HX711 from the components directory
from machine import Pin, SPI  # Importing Pin and SPI modules from the machine directory

# Defining a function to print all properties of an item
def test_list_props(item):
    # Get all the properties of the item
    properties_of_dType = dir(item)
    # Iterate through all the properties
    for property_of_dType in properties_of_dType:
        # Print the property name
        dType.PrintInfo(0, property_of_dType)
        # Delay for 750 milliseconds
        dType.dSleep(750)

# Defining a function to initialize the HX711 module
def init_hx711():
    # Defining the pins for the HX711 module
    pin_OUT = Pin("D12", Pin.IN, pull=Pin.PULL_DOWN)
    pin_SCK = Pin("D13", Pin.OUT)
    spi_SCK = Pin("D13")
    # Connecting to the weight module
    print("Conectando ao modulo de peso")
    Time.sleep(1000)
    # Initializing the SPI connection
    spi = SPI(baudrate=1000000, polarity=0, phase=0, sck=spi_SCK, mosi=pin_SCK, miso=pin_OUT)
    # Initializing the HX711 object
    hx711 = HX711(pin_SCK, pin_OUT, spi)
    # Reading the weight value in a loop
    while True:
        try:
            # Taring the module
            hx711.tare()
            # Reading the value
            hx711.read()
            # Getting the value
            value = hx711.get_value()
            # Printing the value
            print(str(value))       
        except:
            # Printing an error message if the module is not found
            print("Erro: modulo de peso nao encontrado")
        # Delay for 500 milliseconds
        Time.sleep(500)

# Defining a function to turn on the electromagnet
def turnOnElectromagnet(mf):
    # Setting the pin mode
    MagicBox.IO.set_pin_mode(12, magicbox.DO)
    # Delay for 500 milliseconds
    Time.sleep(500)
    # Setting the pin value to 1
    MagicBox.IO.set_pin_value(12, 1)
    # Delay for 500 milliseconds
    Time.sleep(500)
    # Setting the pin mode 
    MagicBox.IO.set_pin_mode(13, magicbox.PWM)
    # Wait 500ms
    Time.sleep(500)
    # Set pin 12 to high
    MagicBox.IO.set_pin_pwm(13, 5000, mf)
    # Wait 500ms
    Time.sleep(500)

# Defining a function to turn off the electromagnet
def turnOffElectromagnet():
    # Setting the pin mode
    MagicBox.IO.set_pin_mode(12, magicbox.DO)
    # Delay for 500 milliseconds
    Time.sleep(500)
    # Setting the pin value to 0
    MagicBox.IO.set_pin_value(12, 0)

# Defining a function to show the position of the Dobot arm
def showPosition():
    # Getting the position of the arm
    position = Dobot.get_pose()
    # Formatting the position
    positionStr = "X {0} Y:{1} Z:{2}".format(position[0], position[1], position[2])
    # Printing the position
    print(positionStr)

# Defining a function to move the Dobot arm to scan the first tray
def scanFirstTray():
    # Printing a message
    print("Scanneando primeira bandeja!")
    # Delay for 500 milliseconds
    Time.sleep(500)
    # Defining the coordinates
    coordinates = [
        [-210,  275,  12, 0,1],
        [342,  52,  12, 0, 1], 
        [310,  51,  12, 0, 1], 
        [-185,  254,  12, 0, 1],   
        [-158,  217,  12, 0, 1],
        [266,  41,  12, 0, 1]
        ]
    # Iterating through all the coordinates
    for i in range(0,6):
        Dobot.move_to(coordinates[i][0],coordinates[i][1],coordinates[i][2],coordinates[i][3],coordinates[i][4])
        Time.sleep(1000)   

def scanSecondTray():
    print("Limpando na segunda bandeja!")    # Prints message on the display
    Time.sleep(500)    # Wait for 500ms before executing the next line of code
    coordinates = [    # List of coordinates to move the Dobot arm to
        [340,  -63,  76, 0, 1],
        [340,  -63,  16, 0, 1],
        [25,  -349,  12, 0, 1], 
        [22,  -310,  12, 0, 1], 
        [308,  -46,  12, 0, 1],
        [264,  -46,  12, 0, 1],
        [26,  -267,  12, 0, 1]
        ]
    for i in range(0,7):    # Loop over the coordinates list and move the Dobot arm to each coordinate
        Dobot.move_to(coordinates[i][0],coordinates[i][1],coordinates[i][2],coordinates[i][3],coordinates[i][4])
        Time.sleep(1000)   # Wait for 1000ms before executing the next line of code

def scanThirdTray():
    print("Despejando na terceira bandeja!")    # Prints message on the display
    coordinates = [    # List of coordinates to move the Dobot arm to
        [-67,  -304,  125, 0,1],
        [-71,  -301,  12, 0,1]
    ]
    for i in range(0,2):    # Loop over the coordinates list and move the Dobot arm to each coordinate
        Dobot.move_to(coordinates[i][0],coordinates[i][1],coordinates[i][2],coordinates[i][3],coordinates[i][4])
        Time.sleep(1000)    # Wait for 1000ms before executing the next line of code
        
    turnOffElectromagnet() 
    repeat = 0   # Turn off the electromagnet
    while repeat !=6:    # Loop over the range 0 to 6
        if (repeat % 2 == 0):    # Check if the index is even
            Dobot.move_to(-71,  -301,  12, 0,1)    # Move the Dobot arm to the first coordinate
        else:
            Dobot.move_to(-211,  -230,  12, 0,1)    # Move the Dobot arm to the second coordinate
        repeat = repeat +1

def upArm():
    position = Dobot.get_pose()    # Get the current position of the Dobot arm
    x = position['x']    # Get the value of x-coordinate
    y = position['y']    # Get the value of y-coordinate
    Time.sleep(1000)    # Wait for 1000ms before executing the next line of code
    Dobot.move_to(x, y,  150, 0)    # Move the Dobot arm to the specified coordinate

def finish():   
    upArm()    # Move the Dobot arm up
    Dobot.set_home()    # Set the current position as home position
    Time.sleep(500)    # Wait for 500ms before executing the next line of code
    print("Ensaio finalizado!")    # Prints message on the display
    play_buzzer()    # Play the buzzer

def set_magnetic_field():
    is_confirm = False # Initialize a flag to check if the magnetic field is confirmed
    magnetic_field = 50 # Set the initial value of the magnetic field to 50
    while(is_confirm == False): # Start a loop until the magnetic field is confirmed
        print("Campo: ", magnetic_field)  # Print the current value of the magnetic field
        if Keyboard.UP.is_pressed() and magnetic_field <100:   # Check if the UP arrow key is pressed and the magnetic field is less than 100
            Time.sleep(1000) # Wait for 1 second
            magnetic_field = magnetic_field + 10 # Increase the magnetic field by 10
            print(str(magnetic_field))   # Print the updated magnetic field value

        if Keyboard.DOWN.is_pressed() and magnetic_field >10:  # Check if the DOWN arrow key is pressed and the magnetic field is greater than 10
            Time.sleep(1000) # Wait for 1 second
            magnetic_field = magnetic_field - 10 # Decrease the magnetic field by 10
            print(str(magnetic_field)) # Print the updated magnetic field value

        if Keyboard.RIGHT.is_pressed(): # Check if the RIGHT arrow key is pressed
            print("Campo escolhido!") # Print a message to confirm that the magnetic field is chosen
            Time.sleep(2000) # Wait for 2 seconds
            is_confirm = True # Set the flag to True to exit the loop
    return magnetic_field # Return the confirmed magnetic field value


def play_buzzer():
    Buzzer.play(200) # Play a sound with a frequency of 200Hz using the buzzer
    Time.sleep(150) # Wait for 150 milliseconds
    Buzzer.play(200) # Play the sound again


def main():
    magnetic_field = set_magnetic_field() # Call the function to set the magnetic field and assign the confirmed value to a variable
    play_buzzer() # Call the function to play the buzzer sound
    Time.sleep(1000) # Wait for 1 second
    print("Iniciando ensaio") # Print a message to indicate that the experiment is starting
    while True: # Start an infinite loop
        isScan = 0 # Initialize a counter to keep track of the number of trays scanned
        while (isScan != 2): # Start a loop until two trays are scanned
            upArm() # Call a function to move the arm to a certain position
            Dobot.set_home() # Set the current position as the home position for the robot
            turnOnElectromagnet(magnetic_field) # Call a function to turn on the electromagnet with the confirmed magnetic field value
            scanFirstTray() # Call a function to scan the first tray
            upArm() # Call a function to move the arm to a certain position
            scanSecondTray() # Call a function to scan the second tray
            upArm() # Call a function to move the arm to a certain position
            scanThirdTray() # Call a function to scan the third tray
            isScan = isScan + 1 # Increase the counter by 1
        finish() # Call a function to finish the experiment
        Time.sleep(2000) # Wait for 2 seconds before starting the next round of the loop
        #init_hx711()
