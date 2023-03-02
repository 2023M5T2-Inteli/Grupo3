
from lib.dobot import Interface
import pygame
import sys
import os

# Include the parent directory in the path so we can import the Dobot library
sys.path.insert(0, os.path.abspath('.'))

# Custom interface port for connection in Dobot
bot = Interface('/dev/ttyACM0')

# Setup variables for joystick event monitoring
clock = pygame.time.Clock()
keepPlaying = True
joysticks = []
#

# Init pygame lib for joystick
pygame.init()

# Verify bot connection status
print('Bot status:', 'connected' if bot.connected() else 'not connected')

# Wait bot connection
while (not bot.connected()):
    pass


# Setup bot parameters for moves
bot.set_jog_joint_params([50, 50, 50, 50], [100, 100, 100, 100])
bot.set_jog_coordinate_params([50, 50, 50, 50], [100, 100, 100, 100])
bot.set_jog_common_params(200, 200)

# Main function for joystick control on bot


def move_control():
    x_p = round(pygame.joystick.Joystick(0).get_axis(4), 1)  # X axis of joystick
    y_p = round(pygame.joystick.Joystick(0).get_axis(3), 1)  # Y axis of joystick
    z_p = round(pygame.joystick.Joystick(0).get_axis(1), 1)  # Z axis of joystick

    # Check joystick axis value and send command to bot
    if y_p > 0.2:
        bot.set_jog_command(1, 2)  # Send command to dobot
    elif y_p < -0.2:
        bot.set_jog_command(1, 1)  # Send command to dobot
    elif x_p > 0.2:
        bot.set_jog_command(1, 4)  # Send command to dobot
    elif x_p < -0.2:
        bot.set_jog_command(1, 3)  # Send command to dobot
    elif z_p > 0.2:
        bot.set_jog_command(1, 5)  # Send command to dobot
    elif z_p < -0.2:
        bot.set_jog_command(1, 6)  # Send command to dobot
    else:  # Stop bot when joystick is not pressed
        bot.set_jog_command(1, 0)  # Send command to dobot

    [x, y, z, r] = bot.get_pose()[0:4]  # Get bot position
    print('FPS: ', clock.get_fps())  # Print FPS
    print(f'Robot position      ➡ \tX:{round(x, 1)} Y:{round(y, 1)} Z:{round(z, 1)}')  # Print bot position
    print(f'JoyStick axis value ➡ \tX:{x_p} Y:{y_p} Z:{z_p}')  # Print joystick axis value
    print('----------------------------------------')  # Print separator


def claw_control():
    suck = pygame.joystick.Joystick(0).get_axis(2) > 0  # Get button value axis 2 ( > 0 for button pressed )
    grip = pygame.joystick.Joystick(0).get_axis(5) > 0  # Get button value axis 5 ( > 0 for button pressed )

    suck = grip if grip else suck  # If grip is pressed, need to enable suck ( dobot thing )

    bot.set_end_effector_gripper(suck, grip)  # Send command to dobot


for i in range(0, pygame.joystick.get_count()):  # Get joystick count
    joysticks.append(pygame.joystick.Joystick(i))  # Append joystick to list
    joysticks[-1].init()  # Init joystick
    print("Detected joystick '", joysticks[-1].get_name(), "'")  # Print joystick name

while keepPlaying:  # Main loop ( while true..)
    clock.tick(300)  # Set FPS for max peformance
    pygame.event.pump()  # Update pygame event
    move_control()  # Control move of dobot with joystick
    claw_control()  # Control claw of dobot with joystick
