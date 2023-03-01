#include <Arduino.h>
#include <HX711.h>

class WeightModule : public HX711 {
public:
	// Constructor and destructor
	WeightModule(byte dout, byte pd_sck, float weight_scale = 1490, byte gain = 128) : HX711() {
		begin(dout, pd_sck, gain);	// Call the HX711 constructor
		set_scale(weight_scale);	// Set the scale
		tare();						// Tare the scale
	}

	virtual ~WeightModule() {}
};
