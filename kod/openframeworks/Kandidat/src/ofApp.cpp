#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup() {
  ofSetCircleResolution(50);
  ofSetFrameRate(45);
  // previousPoint.set(theCircle);
  // points = new std::vector<ofVec2f>();
  receiver.setup(OSC_PORT);
  // points = {ofVec2f(0.0, 0.0), ofVec2f(0.0, 0.0), ofVec2f(0.0, 0.0)};

  theCircle.set(ofGetWidth() / 2, ofGetHeight() / 2);
  points.push_back(theCircle);
  velocity.set(1.f, 1.f);
  velocity.normalize();
  velocity.scale(10.f);
  // ofSetBackgroundAuto(false);
}

//--------------------------------------------------------------
// buffra datan
void ofApp::update() {
  while (receiver.hasWaitingMessages()) {
    ofxOscMessage message;
    receiver.getNextMessage(&message);
    if (!isDataReceived)

      if (message.getAddress() == "/value")
        values.push_back(message.getArgAsFloat(0));
      else if (message.getAddress() == "/time")
        times.push_back(message.getArgAsInt(0));
      else if (message.getAddress() == "/done") {
        isDataReceived = true;
        // dataThread.setReceivedData(values);
        // dataThread.startThread();
      }
  }
  if (isDataReceived /*&& ofGetElapsedTimef() >= lastTime + 0.1*/) {
    // lastTime = ofGetElapsedTimef();
    velocity = velocity.getRotated(values[counter] - 10.f);
    theCircle += velocity;
    counter = (counter + 1) % values.size();
    if (theCircle.x > ofGetWidth() + 10) {
      theCircle.x = 0;
      // points.insert(points.begin(), theCircle);
      // previousPoint.set(theCircle);

    } else if (theCircle.x < -10) {
      theCircle.x = ofGetWidth();
      // points.insert(points.begin(), theCircle);
      // previousPoint.set(theCircle);
    }
    if (theCircle.y > ofGetHeight() + 10) {
      theCircle.y = 0;
      // points.insert(points.begin(), theCircle);
      // previousPoint.set(theCircle);

    } else if (theCircle.y < -10) {
      theCircle.y = ofGetHeight();
      // points.insert(points.begin(), theCircle);
      // previousPoint.set(theCircle);
    }
    points.insert(points.begin(), theCircle);
    while (points.size() > LINE_SEGMENTS)
      points.pop_back();
  }
}

//--------------------------------------------------------------
void ofApp::draw() {
  ofEnableAlphaBlending();
  ofFill();

  for (size_t i = 0; i < MIN(LINE_SEGMENTS, points.size() - 1); i++) {
    ofSetColor(255, 255, 255, ofMap(i, 0, LINE_SEGMENTS, 255, 0, true));
    ofVec2f currentPoint = points[i + 1], lastPoint = points[i];
    if (currentPoint.distance(lastPoint) <
        (MIN(ofGetWidth(), ofGetHeight()) - 50))
      ofDrawLine(currentPoint, lastPoint);
  }
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key) {}

//--------------------------------------------------------------
void ofApp::keyReleased(int key) {}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y) {}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button) {}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button) {}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button) {}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y) {}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y) {}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h) {}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg) {}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo) {}
// void ofApp::exit() { dataThread.stopThread(); }
