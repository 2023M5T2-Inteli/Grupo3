#include <Arduino.h>

enum Direction { FORWARD = 1, BACKWARD = -1, STOP = 0 };

class HBridge {
private:
	void setInValues(bool in1_pin, bool in2_pin);
	void setPwmValue(byte pwm_pin);

	byte m_pwmPin;
	byte m_in1Pin;
	byte m_in2Pin;

public:
	HBridge(byte pwm_pin, byte in1_pin, byte in2_pin);
	~HBridge();

	void setDuty(byte duty);
	void setDirection(Direction direction);
};
