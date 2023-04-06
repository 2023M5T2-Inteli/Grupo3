from machine import Pin
import time
import pyb

# m_lite.set_ptpcmd(ptp_mode=0, x=250, y=0, z=50, r=0)
# m_lite.set_homecmd()
# m_lite.set_endeffector_suctioncup(enable=True, on=True)
# m_lite.set_endeffector_gripper(enable=True, on=True)
# m_lite.get_pose()
# m_lite.wait(delay=10)
# m_lite.set_armspeed_ratio(set_type=1, set_value=50)
# m_lite.clean_alarm()

# magicbox.set_emotor(index=1, enable=True, speed=50)
# magicbox.set_port(port=1, io_func=magicbox.DUMMY)
# magicbox.set_io(port=1, level=1)
# magicbox.set_pwm(port=1, frequency=10.2, duty_cycle=30.0)
# magicbox.get_di(port=1)
# magicbox.get_do(port=1)
# magicbox.get_ad(port=1)

# magicbox.set_oled_clear(port=1)
# magicbox.set_oled_pos_text(port=1, n=1, m=1, text="hello")
# magicbox.set_oled_text(port=1, text="hello")

# magicbox.set_tts_effect(port=2, index=1)
# magicbox.set_tts_music(port=2, index=1)
# magicbox.set_tts_tone(port=2, index=1)
# magicbox.set_tts_volume(port=2, sound=5)
# magicbox.set_tts_cmd(port=2, cmd=0)

# magicbox.get_knob_value(port=3)
# magicbox.get_sound_value(port=3)
# magicbox.get_joystick_button(port=2)
# magicbox.get_joystick_pos(port=2)
# magicbox.get_button_status(port=1)

'''
E3 = UP
C13 = DOWN
C15 = LEFT
C14 = RIGHT
D4 = CENTER

E10 = BUZZER

D13 = RIGHT P5
D12 = LEFT P5
'''


def get_pins():
   return dir(pyb.Pin.cpu)[2:]


last_pins_state = {}
try:
   while True:
       for pin in get_pins():
           pin_instance = Pin(pin)
           if pin_instance.value() != last_pins_state.get(str(pin), None):
               print('changed ' + str(pin) + '=' + str(pin_instance.value()))
               last_pins_state[str(pin)] = pin_instance.value()
       print('loop end')
       time.sleep(2)
except Exception as e:
   print(e)
'''
E3 = UP
C13 = DOWN
C15 = LEFT
C14 = RIGHT
D4 = CENTER


E10 = BUZZER

D13 = RIGHT P5
D12 = LEFT P5
'''
