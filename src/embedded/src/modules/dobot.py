from base.api import *


class Dobot:
    @staticmethod
    def move_to(x: float, y: float, z: float, r: float, mode:int=0) -> None:
        '''
        x: the x coordinate
        y: the y coordinate
        z: the z coordinate
        r: the rotation head coordinate
        '''
        # 0: JUMP mode, (x, y, z, r) is the coordinates of a target point under the Cartesian coordinate system
        m_lite.set_ptpcmd(mode, x, y, z, r)

    @staticmethod
    def get_pose() -> dict:
        return m_lite.get_pose()

    @staticmethod
    def get_alarms() -> list:
        return m_lite.get_lost_step_result()

    @staticmethod
    def clear_alarms() -> None:
        m_lite.clean_alarm()

    @staticmethod
    def set_home() -> None:
        m_lite.set_homecmd()
