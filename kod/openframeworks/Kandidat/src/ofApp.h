#pragma once

#include "DataThread.h"
#include "ofMain.h"
#include "ofMath.h"
#include "ofxOsc.h"
#include <vector>

#define OSC_PORT 7771
#define LINE_SEGMENTS 200

class ofApp : public ofBaseApp {

public:
  void setup();
  void update();
  void draw();

  void keyPressed(int key);
  void keyReleased(int key);
  void mouseMoved(int x, int y);
  void mouseDragged(int x, int y, int button);
  void mousePressed(int x, int y, int button);
  void mouseReleased(int x, int y, int button);
  void mouseEntered(int x, int y);
  void mouseExited(int x, int y);
  void windowResized(int w, int h);
  void dragEvent(ofDragInfo dragInfo);
  void gotMessage(ofMessage msg);
  void exit() {}

private:
  ofxOscReceiver receiver;
  std::vector<ofVec2f> *points;
  std::vector<float> values;
  std::vector<int> times;
  bool isDataReceived = false;
  DataThread dataThread;
};
