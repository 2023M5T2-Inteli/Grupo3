import dType


class Dobot:
    @staticmethod
    def setup() -> None:
        dType.SetQueuedCmdClear(0)  # clear the command queue
        dType.SetQueuedCmdStopExec(0)  # stop the command queue
        dType.SetQueuedCmdStartExec(0)  # start the command queue
        dType.SetArmSpeedRatio(0, 1, 30, 1)  # set the arm speed
        dType.SetLostStepParams(0, 5.0, 1)  # set the lost step parameters

    @staticmethod
    def move_to(x: float, y: float, z: float, r: float) -> None:
        '''
        x: the x coordinate
        y: the y coordinate
        z: the z coordinate
        r: the rotation head coordinate
        '''
        dType.SetPTPCmdEx(0, 1, x, y, z, r, 1)  # 2 is the PTP mode

    @staticmethod
    def set_servo(servoId: int, angle: int) -> None:
        '''
        servoId: the servo ID
        angle: the angle to set the servo to
        '''
        dType.SetServoAngleEx(0, servoId, angle, 1)

    @staticmethod
    def get_pose() -> list[float]:
        return dType.GetPose(0)

    @staticmethod
    def get_alarms() -> list[int]:
        return dType.GetAlarmsState(0)

    @staticmethod
    def clear_alarms() -> None:
        dType.ClearAllAlarmsState(0)

    @staticmethod
    def set_home() -> None:
        dType.SetHOMECmdEx(0, 0, 1)