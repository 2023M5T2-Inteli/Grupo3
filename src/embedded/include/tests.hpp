#include <Arduino.h>

#include "components/HBridge.hpp"
#include "components/weightModule.hpp"

void test_WeightModule() {
	WeightModule weightModule(3, 2);

	while (true) {
		Serial.print("Reading:\t");
		Serial.print(weightModule.get_units(), 1);
		Serial.println("g");
		delay(100);
	}
}

void test_HBridge() {
	HBridge hbridge(5, 6, 7);

	hbridge.setDuty(100);
	hbridge.setDirection(Direction::FORWARD);

	while (true) {
	}
}