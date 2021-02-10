var server ;
var values = List.new();

var oscFunc = {

	arg msg, time, addr, recvPort;

	switch(msg[0],
		'/value', {values.add(msg[1]);},
		'/valueDone', {
			fork {
				values.do({
					arg val;
					Synth.new(\sin, [\freq, Scale.majorPentatonic.degreeToFreq(val.clip(1,20), 220, 0)], target: server);
					val.linlin(1,20,0.75,0.125).wait;
				});
			};
		}
	);

};

var serverOptions = ServerOptions.new;

SynthDef.new(\sin,  {
	arg freq;
	var sinOsc = SinOsc.ar(freq, mul:0.1)*EnvGen.kr(Env.perc(), doneAction: Done.freeSelf);
	Out.ar(0, sinOsc!2);
}).add;

serverOptions.device = "scjack:supercollider";
serverOptions.numInputBusChannels = 0;

"SC_JACK_DEFAULT_INPUTS".setenv();
"SC_JACK_DEFAULT_OUTPUTS".setenv("darkice-piano");

server = Server.new(\diabetesServer,  NetAddr("localhost", 58009),  options: serverOptions);

SynthDescLib.global.addServer(server);

thisProcess.addOSCRecvFunc(oscFunc);

server.boot;
