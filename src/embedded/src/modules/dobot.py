# Importing required modules from base.api
from base.api import *

# Defining a class for Dobot
class Dobot:
    # Method to move Dobot to a given (x, y, z) position and rotation head coordinate (r)
    @staticmethod
    def move_to(x: float, y: float, z: float, r: float, mode:int=0) -> None:
        '''
        x: the x coordinate
        y: the y coordinate
        z: the z coordinate
        r: the rotation head coordinate
        '''
        # Setting the target point for Dobot to move to, with the given (x, y, z, r) coordinates and mode (0: JUMP mode)
        m_lite.set_ptpcmd(mode, x, y, z, r)

    # Method to get the current pose of Dobot (position and orientation)
    @staticmethod
    def get_pose() -> dict:
        # Returning the current pose of Dobot as a dictionary
        return m_lite.get_pose()

    # Method to get the list of alarms (if any) occurred during the movement of Dobot
    @staticmethod
    def get_alarms() -> list:
        # Returning the list of alarms (if any) occurred during the movement of Dobot
        return m_lite.get_lost_step_result()

    # Method to clear the alarms (if any) occurred during the movement of Dobot
    @staticmethod
    def clear_alarms() -> None:
        # Clearing the alarms (if any) occurred during the movement of Dobot
        m_lite.clean_alarm()

    # Method to set the current position and orientation of Dobot as the home position
    @staticmethod
    def set_home() -> None:
        # Setting the current position and orientation of Dobot as the home position
        m_lite.set_homecmd()
