#include "components/HBridge.hpp"

HBridge::HBridge(byte pwm_pin, byte in1_pin, byte in2_pin) {
	this->m_pwmPin = pwm_pin;
	this->m_in1Pin = in1_pin;
	this->m_in2Pin = in2_pin;

	pinMode(this->m_pwmPin, OUTPUT);
	pinMode(this->m_in1Pin, OUTPUT);
	pinMode(this->m_in2Pin, OUTPUT);

	this->setInValues(false, false);
	this->setPwmValue(0);
}

HBridge::~HBridge() {
	this->setInValues(false, false);
	this->setPwmValue(0);
}

void HBridge::setInValues(bool in1_pin, bool in2_pin) {
	digitalWrite(this->m_in1Pin, in1_pin);
	digitalWrite(this->m_in2Pin, in2_pin);
}

void HBridge::setPwmValue(byte pwm_pin) { analogWrite(this->m_pwmPin, pwm_pin); }

void HBridge::setDuty(byte duty) {
	// duty is a value between 0 and 100
	// map the duty value to a value between 0 and 255 to use with analogWrite
	// constrain the value between 0 and 255 to avoid errors
	this->setPwmValue(constrain(map(duty, 0, 100, 0, 255), 0, 255));
}

void HBridge::setDirection(Direction direction) {
	// direction is a value between -1, 0 and 1
	// direction FORWARD: IN1 = HIGH, IN2 = LOW
	// direction STOP: IN1 = LOW, IN2 = LOW
	// direction BACKWARD: IN1 = LOW, IN2 = HIGH

	switch (direction) {
		case FORWARD:
			this->setInValues(true, false);
			break;
		case BACKWARD:
			this->setInValues(false, true);
			break;
		case STOP:
			this->setInValues(false, false);
			break;
	}
}
