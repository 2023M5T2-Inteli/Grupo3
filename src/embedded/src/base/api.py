
# inject api
import _thread
import mb
import dType
import rtt
import time
import os
import mgo
import mgl
import pyb
import kca
import math
import mg


class MbApi(object):
    STP1 = 0
    STP2 = 1
    DUMMY = 0
    DO = 1
    PWM = 2
    DI = 3
    ADC = 4
    DIPU = 5
    DIPD = 6

    # 摇杆传感器接口参数status
    BTN_UP = 0
    BTN_DOWN = 1
    BTN_LEFT = 2
    BTN_RIGHT = 3
    BTN_MIDDLE = 4

    # 手势传感器接口传参ges
    RIGHT = 1
    LEFT = 2
    UP = 4
    DOWN = 8
    FORWARD = 16
    BACKWARD = 32
    CLOCKWISE = 64
    ANTICLOCKWISE = 128

    def set_emotor(self, index, enable, speed):
        if enable:
            mb.SetEMotor(index, 1, speed)
            return True
        else:
            mb.SetEMotor(index, 0, speed)
            return True

    def set_color_sensor(self, port, enable, version):
        if enable:
            mb.SetColorSensor(1, port - 1, version)
            return True
        else:
            mb.SetColorSensor(0, port - 1, version)
            return True

    def get_color_sensor(self):
        r = mb.GetColorSensor(0)
        g = mb.GetColorSensor(1)
        b = mb.GetColorSensor(2)
        res = {'red': r, 'green': g, 'blue': b}
        return res

    def set_infrared_sensor(self, port, enable, version):
        if enable:
            mb.SetInfraredSensor(1, port - 1, version)
            return True
        else:
            mb.SetInfraredSensor(0, port - 1, version)
            return True

    def get_infrared_sensor(self, port):
        res = mb.GetInfraredSensor(port - 1)
        sensor_res = {'status': res}
        return sensor_res

    def set_device_withl(self, enable, version):
        mb.SetDeviceWithL(enable, version)
        return True

    def set_ptpwithl_cmd(self, set_l):
        res = mgl.GetPose(0)
        mb.SetPTPWithLCmd(1, res[0], res[1], res[2], res[3], set_l, 0)
        return True

    def set_lspeed_ratio(self, set_value):
        mb.SetQueuedCmdStartExec()
        mb.SetLSpeedRatio(1, set_value, 0)
        return True

    def get_posel(self):
        res = mb.GetPoseL()
        return res

    def set_led_rgb(self, port, index, red, green, blue):
        mb.DobotSensorSetRGBLEDValue(port - 1, index - 1, red, green, blue)
        return True

    def set_led_color(self, port, index, color: str, value):
        color_list = {"red": 0, "green": 1, "blue": 2, "yellow": 3, "white": 4}
        mb.DobotSensorSetRGBLEDColor(port - 1, index - 1, color_list[color],
                                     value)
        return True

    def set_led_state(self, port, index, on):
        if on:
            mb.DobotSensorSetRGBLEDState(port - 1, index - 1, 1)
        else:
            mb.DobotSensorSetRGBLEDState(port - 1, index - 1, 0)
        return True

    def set_tts_play(self, port, text):
        mb.DobotSensorSendSYN(port - 1, text)
        return True

    def set_tts_volume(self, port, sound):
        mb.DobotSensorSetSYN(port - 1, sound)
        return True

    def set_tts_music(self, port, index):
        mb.DobotSensorSetSYNMusic(port - 1, 0, index - 1)
        return True

    def set_tts_effect(self, port, index):
        mb.DobotSensorSetSYNMusic(port - 1, 1, index - 1)
        return True

    def set_tts_tone(self, port, index):
        mb.DobotSensorSetSYNMusic(port - 1, 2, index - 1)
        return True

    def set_tts_cmd(self, port, cmd):
        mb.DobotSensorSetSYNCmd(port - 1, cmd)
        return True

    def set_oled_text(self, port, text):
        mb.DobotSensorOledShow(port - 1, text)
        return True

    def set_oled_pos_text(self, port, n, m, text):
        mb.DobotSensorOledDisplay(port - 1, n - 1, m - 1, text)
        return True

    def set_oled_clear(self, port):
        mb.DobotSensorOledClear(port - 1)
        return True

    def get_knob_value(self, port):
        return mb.DobotSensorGetKnob(port - 1)

    def get_light_value(self, port):
        return mb.DobotSensorGetLight(port - 1)

    def get_sound_value(self, port):
        return mb.DobotSensorGetVoice(port - 1)

    def get_humiture_value(self, port):
        return mb.DobotSensorGetSHT31(port - 1)

    def get_color_value(self, port, index):
        return mb.DobotSensorGetColor(port - 1, index)

    def get_color_result(self, port):
        if mb.DobotSensorGetColorIsTrue(port - 1, 1):
            return "red"
        elif mb.DobotSensorGetColorIsTrue(port - 1, 2):
            return "green"
        elif mb.DobotSensorGetColorIsTrue(port - 1, 3):
            return "blue"
        elif mb.DobotSensorGetColorIsTrue(port - 1, 4):
            return "yellow"
        elif mb.DobotSensorGetColorIsTrue(port - 1, 5):
            return "black"
        elif mb.DobotSensorGetColorIsTrue(port - 1, 6):
            return "white"
        else:
            return None

    def get_photoelectric_switch_value(self, port):
        mb.SetInfraredSensor(1, port - 1, 1)
        return mb.GetInfraredSensor(port - 1)

    def set_port(self, port, io_func):
        mb.SetIOMultiplexing(port, multiplex=io_func)
        return True

    def set_converyor(self, index, enable, speed):
        STEP_PER_CIRCLE = 360.0 / 1.8 * 5.0 * 16.0
        MM_PER_CIRCLE = 3.1415926535898 * 32
        vel = STEP_PER_CIRCLE / MM_PER_CIRCLE
        if enable:
            mb.SetEMotor(index, 1, int(math.floor(speed * vel)))
            return True
        else:
            mb.SetEMotor(index, 0, int(speed))
            return True

    def set_io(self, port, level):
        mb.SetIODO(port, level)
        return True

    def set_pwm(self, port, frequency, duty_cycle):
        mb.SetIOPWM(port, frequency, duty_cycle)
        return True

    def get_do(self, port=1):
        res = mb.GetIODO(port)
        return {"port": port, "level": res}

    def get_di(self, port):
        res = mb.GetIODI(port)
        return {"port": port, "level": res}

    def get_ad(self, port):
        res = mb.GetIOADC(port)
        return {"port": port, "level": res}

    def set_rail(self, enable, version, speed_ratio):
        if enable:
            mb.SetDeviceWithL(1, version)
            mb.SetLSpeedRatio(1, speed_ratio, 0)
        else:
            mb.SetDeviceWithL(0, version)
            mb.SetLSpeedRatio(1, speed_ratio, 0)
        return True

    def set_rail_ptpcmd(self, distance):
        pose_res = mgl.GetPose(0)
        mb.SetPTPWithLCmd(0, pose_res[0], pose_res[1], pose_res[2],
                          pose_res[3], distance, 0)
        return True

    def get_rail_speed_ratio(self):
        return mb.GetLSpeedRatio(1)[1]

    def get_pixy_camera_obj(self, port, color, coordinate):
        res = mb.GetPixyBlockValue(port, color, coordinate)
        return {"color": res[0], "coordinate": res[1]}

    def get_pixy_camera_is_detected(self, port, color):
        res = mb.PixyBlockIsExist(port, color)
        if res == 1:
            return True
        else:
            return False

    def set_bt_mesh(self, group, id):
        mb.SetBleMesh(group, id)
        return True

    def set_bt_send(self, to_id, text):
        mb.WriteBleMeshData(text, to_id)
        return True

    def get_bt_receive(self, from_id):
        res = mb.ReadBleMeshData(from_id)
        if res == 0:
            return None
        return res

    def get_bt_is_received(self, from_id, text):
        res = mb.IsReceiveStr(from_id, text)
        if res == 1:
            return True
        return False

    def get_bt_until_received(self, from_id, text):
        while 1:
            res = mb.IsReceiveStr(from_id, text)
            if res == 1:
                break
            time.sleep(0.5)
        return True

    def clean_bt_cache(self):
        mb.BleClearMeshData()
        return True

    def get_ges_result(self, port):
        mb.DobotSensorGestureInit(port - 1)
        return mb.DobotSensorGetGestureData(port - 1)

    def is_ges_detected(self, port, ges):
        mb.DobotSensorGestureInit(port - 1)
        return mb.DobotSensorGetGestureResult(port-1, ges)

    def is_joystick_button(self, port, index):
        return mb.is_joystick_button(port-1, index)

    def get_joystick_button(self, port: int):
        return mb.get_joystick_button(port-1)

    def get_joystick_pos(self, port: int):
        res = mb.get_joystick_pos(port-1)
        return {"x": res[0], "y": res[1], "z": res[2]}

    def is_pir_detected(self, port):
        return mb.is_pir_detected(port-1)

    def set_servo_angle(self, port, angle):
        return mb.SetServoAngle(port-1, angle)

    def get_button_status(self, port):
        return mb.get_button_status(port-1)


def print(*res):
    tem_res = ""
    for i in range(len(res)):
        tem_res += str(res[i]) + " "
    # mb.PrintInfo(str(tem_res))
    dType.PrintInfo(0, (str(tem_res)))


magicbox = MbApi()


# inject api
class MliteApi(object):
    JOG = 0
    PTP = 1
    CP = 2
    ARC = 3

    def get_pose(self):
        res = mgl.GetPose(0)
        pose_res = {
            'jointAngle': [res[4], res[5], res[6], res[7]],
            'x': res[0],
            'y': res[1],
            'z': res[2],
            'r': res[3]
        }
        return pose_res

    def set_homecmd(self):
        mgl.SetQueuedCmdStartExec()
        mgl.SetHOMECmd(0, 0, 1)
        return True

    def set_endeffector_suctioncup(self, enable, on):
        if enable:
            if on:
                mgl.SetEndEffectorSuctionCup(1, 1, 0)
                return True
            else:
                mgl.SetEndEffectorSuctionCup(1, 0, 0)
                return True
        else:
            mgl.SetEndEffectorSuctionCup(0, 0, 0)
            return True

    def set_endeffector_gripper(self, enable, on):
        if enable:
            if on:
                mgl.SetEndEffectorGripper(0, 1, 1, 1, 2)
                return True
            else:
                mgl.SetEndEffectorGripper(0, 1, 0, 1, 2)
                return True
        else:
            mgl.SetEndEffectorGripper(0, 0, 0, 1, 2)
            return True

    def set_ptpcmd(self, ptp_mode, x, y, z, r):
        mgl.SetQueuedCmdStartExec()
        mgl.SetPTPCmd(ptp_mode, x, y, z, r, 0, 1)
        return True

    def set_ptpjump_params(self, z_limit, jump_height):
        mgl.SetPTPJumpParams(jump_height, z_limit)
        return True

    def set_armspeed_ratio(self, set_type, set_value):
        mgl.SetArmSpeedRatio(set_type, set_value)
        return True

    def get_armspeed_ratio(self, get_type):
        res = mgl.GetArmSpeedRatio(get_type)
        return {"type": get_type, "value": res[0]}

    def set_arm_speed_ratio(self, mode, speed_ratio):
        mgl.SetArmSpeedRatio(mode, speed_ratio)
        return True

    def set_lost_step_params(self, value):
        mgl.SetLostStepParams(value)
        return True

    def set_lost_step_cmd(self):
        mgl.SetLostStepCmd()
        return True

    def get_lost_step_result(self):
        return mgl.GetAllAlarmsState()

    def clean_alarm(self):
        mgl.ClearAllAlarmsState()
        return True

    def wait(self, delay):
        mgl.SetWAITCmd(1, delay*1000)
        return True

    def get_end_effector_type(self):
        return mgl.GetEndEffectorType()

    def get_arm_speed_ratio(self, mode):
        res = mgl.GetArmSpeedRatio(mode)
        return res[0]


m_lite = MliteApi()


# inject api
class MgApi(object):
    def __init__(self):
        self.rgb_number = {
            "LED_1": 1,
            "LED_2": 2,
            "LED_3": 3,
            "LED_4": 4,
            "LED_ALL": 5
        }

    def set_running_mode(self, mode):
        mgo.SetRunMode(mode)
        return True

    def set_move_speed_direct(self, direction, speed):
        mgo.SetDirSpeed(direction, speed)
        return True

    def set_move_speed(self, x, y, r):
        mgo.SetSpeed(x, y, r)
        return True

    def set_rotate(self, r, Vr):
        mgo.SetQueuedCmdStartExec()
        mgo.SetMoveAngleEx(r, Vr)
        return True

    def set_move_dist(self, x, y, Vx, Vy):
        mgo.SetQueuedCmdStartExec()
        mgo.SetMoveDistanceEx(x, y, Vx, Vy)
        return True

    def set_move_pos(self, x, y, s):
        mgo.SetQueuedCmdStartExec()
        res = mgo.ReadOdom()
        mgo.SetMoveAngleEx(-res[2], s)
        mgo.SetAbsolutePositionEx(x, y, s)
        return True

    def set_arc_rad(self, velocity, radius, angle, mode):
        mgo.SetQueuedCmdStartExec()
        mgo.SetRadiusCircleTrajEx(velocity, radius, angle, mode)
        return True

    def set_arc_cent(self, velocity, x, y, angle, mode):
        mgo.SetQueuedCmdStartExec()
        mgo.SetPointCircleTrajEx(velocity, x, y, angle, mode)
        return True

    def set_coord_closed_loop(self, isEnable, angle):
        mgo.SetWorldCoordinateAng(isEnable, angle)
        return True

    def set_rgb_light(self, number, effect, r, g, b, cycle, counts):
        if type(number) == str:
            mgo.SetRGBColor(self.rgb_number[number], effect, r, g, b, cycle,
                            counts)
            return True
        else:
            mgo.SetRGBColor(number, effect, r, g, b, cycle, counts)
            return True

    def set_buzzer_sound(self, index, tone, beat):
        mgo.SetBuzzer(index, tone, beat)
        return True

    def set_increment_closed_loop(self, x, y, angle):
        mgo.SetQueuedCmdStartExec()
        mgo.SetPOSAngleClosedLoopEx(x, y, angle)
        return True

    def get_ultrasonic_data(self):
        res = mgo.ReadUltrasound()
        return {
            "front": res[0],
            "back": res[1],
            "left": res[2],
            "right": res[3]
        }

    def set_odometer_data(self, x, y, yaw):
        mgo.WriteOdom(x, y, yaw)
        return True

    def get_odometer_data(self):
        res = mgo.ReadOdom()
        return {"x": res[0], "y": res[1], "yaw": res[2]}

    def get_power_voltage(self):
        res = mgo.Power()
        return {"powerVoltage": res[0], "powerPercentage": res[1]}

    def get_imu_angle(self):
        res = mgo.ReadOrientation()
        return {"yaw": res[0], "roll": res[1], "pitch": res[2]}

    def set_auto_trace(self, trace):
        self._kca_init()
        mgo.SetFollowLine(trace)
        return True

    def set_trace_speed(self, speed):
        mgo.SetTraceSpeed(speed)
        return True

    def set_trace_pid(self, p, i, d):
        mgo.SetK210TracePID(p, i, d)
        return True

    def _kca_init(self):
        kca.OpenDataRefreshSign_UART(1, 1)
        kca.OpenDataRefreshSign_UART(1, 0)

    def get_trace_angle(self):
        self._kca_init()
        res = kca.GetTracingData_UART(0)
        return {"angle": res}

    def get_arm_camera_obj(self):
        self._kca_init()
        res = kca.GetAllSignState_UART(1)
        count = res[0]
        res.pop(0)
        return {"count": count, "dl_obj": res}

    def get_car_camera_obj(self):
        self._kca_init()
        res = kca.GetAllSignState_UART(0)
        count = res[0]
        res.pop(0)
        return {"count": count, "dl_obj": res}

    def get_arm_camera_tag(self):
        self._kca_init()
        res = kca.GetAllApilTagData_UART(1)
        count = res[0]
        res.pop(0)
        return {"count": count, "aptag_obj": res}


go = MgApi()


# inject api
class MagicianOfflineApi(object):
    def set_home(self):
        mg.SetHOMECmd(1, 1)
        return True

    def ptp(self, mode, x, y, z, r):
        array_in = [x, y, z, r]
        mg.SetPTPCmd(1, mode, array_in)
        return True

    def set_r(self, r):
        temp = mg.GetPose()
        temp_in = [temp[4], temp[5], temp[6], r]
        mg.SetPTPCmd(1, 2, temp_in)
        return True

    def motion_params(self, velocityRatio, accelerationRatio):
        mg.SetPTPCommonParams(velocityRatio, accelerationRatio)
        return True

    def jump_params(self, zLimit, jumpHeight):
        mg.SetPTPJumpParams(jumpHeight, zLimit)
        return True

    def set_endeffector_suctioncup(self, enable, on):
        if enable:
            if on:
                mg.SetEndEffectorSuctionCup(1, 1)
                return True
            else:
                mg.SetEndEffectorSuctionCup(1, 0)
                return True
        else:
            mg.SetEndEffectorSuctionCup(0, 0)
            return True

    def set_endeffector_gripper(self, enable, on):
        if enable:
            if on:
                mg.SetEndEffectorGripper(1, 1)
                return True
            else:
                mg.SetEndEffectorGripper(1, 0)
                return True
        else:
            mg.SetEndEffectorGripper(0, 0)
            return True

    def get_pose(self):
        res = mg.GetPose()
        pose_res = {
            'jointAngle': [res[4], res[5], res[6], res[7]],
            'x': res[0],
            'y': res[1],
            'z': res[2],
            'r': res[3]
        }
        return pose_res

    def clear_alarm(self):
        mg.ClearAllAlarmsState()
        return True

    def set_lost_step_cmd(self):
        mg.SetLostStepCmd()
        return True

    def set_lost_step_params(self, value):
        mg.SetLostStepParams(value)
        return True

    def wait(self, second):
        mg.SetWAITCmd(1, second*1000)
        return True

    def get_lost_step_result(self):
        return mg.GetAllAlarmsState()

    def get_arm_speed_ratio(self, mode):
        res = mg.GetArmSpeedRatio(mode)
        return res[0]


magician = MagicianOfflineApi()
