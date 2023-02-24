#include <Arduino.h>
#include <HX711.h>

class WeightModule : public HX711 {
public:
	WeightModule(byte dout, byte pd_sck, float weight_scale = 1490, byte gain = 128) : HX711() {
		begin(dout, pd_sck, gain);
		set_scale(weight_scale);
		tare();
	}

	virtual ~WeightModule() {}
};
