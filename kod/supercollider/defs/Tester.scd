
/**
*
* Kod för att test-spela alla SynthDefs 
*
**/
(
	~booted = false;
	~slices = [];
	~buffers = [];
)
(
	Server.default.waitForBoot({
		var wavetable, jlc, drums, radioStretch;
		var order = [8, 28, 21, 3, 25, 13, 23, 1, 22, 29, 9, 2, 17, 5, 10, 7, 12, 4, 6, 27, 26, 19, 20, 14, 16, 24, 30, 18, 15, 11];

		var scale = Scale.phrygian;


		if(~booted != true){
			Buffer.freeAll(s);
			~slices = SoundFile.collectIntoBuffers(File.getcwd +/+ "media/normalized/*",  server: Server.default);
			(File.getcwd +/+ "SynthDefs.sc").load(); //load Synth Defs
			Server.default.sync;
			~booted = true;

			 order.do({ // TODO mirror? setting?
				arg index, count;
				var url = format(File.getcwd +/+ "media/wavetable/sample_%.wav", index); //put samples somewhere else... 
				url.postln;
				~buffers.add(Buffer.read(s, path: url, numFrames: 512)); 
			 });
        };

		wavetable = Synth.new(\Diabetes, [\bufferNum, ~buffers[12].bufnum]);

		for (1, 30) { |i|
			drums = Synth.new(\sliceBuffer, [\bufnum, ~slices.choose.bufnum, \freq, scale.degreeToFreq(-10+20.rand, 220, 0)]);
			[1/3, 1/4, 1/8].wchoose([3,4,5].normalizeSum).wait;
		};

	});
)
~buffers

Server.default.freeAll;
Server.default.queryAllNodes;

