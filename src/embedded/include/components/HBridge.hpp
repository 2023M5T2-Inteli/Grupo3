#include <Arduino.h>

// Define the direction of the motor (forward, backward or stop)
enum Direction { FORWARD = 1, BACKWARD = -1, STOP = 0 };

class HBridge {
private:
	// Private methods for controlling the H-Bridge
	void setInValues(bool in1_pin, bool in2_pin);
	void setPwmValue(byte pwm_pin);

	// Pin numbers
	byte m_pwmPin;
	byte m_in1Pin;
	byte m_in2Pin;

public:
	// Constructor and destructor
	HBridge(byte pwm_pin, byte in1_pin, byte in2_pin);
	~HBridge();

	// Public methods for controlling the H-Bridge
	void setDuty(byte duty);
	void setDirection(Direction direction);
};
