(
Server.default.waitForBoot({
	var object = BloodGlucose.new;
	var routine = 
		Routine({
			loop {
				object.play();
				[1/4, 1/3, 3/7].choose.yield;
			};
		});

	/**
	* Temporary helper definition
	*/
	SynthDef.new(\sinHelper, {
		arg freq = 220;
		var signal = SinOsc.ar(freq, mul: 0.01);
		var env = EnvGen.ar(Env.perc(attackTime: Rand(0.001, 0.01), releaseTime: 1.5), doneAction: Done.freeSelf);
		var outSignal = PanX.ar(2, in: signal*env, pos: Rand(0.0, 1.0));
		Out.ar(0, outSignal);
	}).add;

	Server.default.sync; //to make sure synthdef is properly loaded..

	object.scale = Scale.yu;
	object.setTuning(\just);
	object.soundSource = 'sinHelper';
	routine.play;

});
)

Server.default.queryAllNodes;
