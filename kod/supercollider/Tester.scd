(
Server.default.waitForBoot({
	var object = BloodGlucose.new;

	/**
	* Temporary helper definition
	*/
	SynthDef.new(\sinHelper, {
		arg freq = 220;
		Out.ar(0, SinOsc.ar(freq, mul: 0.01)!2);
	}).add;

	Server.default.sync;

	object.scale = Scale.yu;
	object.soundSource = Synth.new(\sinHelper);
	object.parseOsc("hello world").postln;

});
)
