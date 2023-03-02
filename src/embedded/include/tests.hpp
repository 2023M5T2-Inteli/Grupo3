#include <Arduino.h>

#include "components/HBridge.hpp"
#include "components/weightModule.hpp"

void test_WeightModule() {
	WeightModule weightModule(3, 2);  // DOUT, PD_SCK

	// Main loop
	while (true) {
		Serial.print("Reading:\t");
		Serial.print(weightModule.get_units(), 1);
		Serial.println("g");
		delay(100);
	}
}

void test_HBridge() {
	HBridge hbridge(5, 6, 7);  // PWM, IN1, IN2

	// Set the duty cycle to 100% and the direction to forward
	hbridge.setDuty(100);
	hbridge.setDirection(Direction::FORWARD);

	// Main loop
	while (true) {
	}
}