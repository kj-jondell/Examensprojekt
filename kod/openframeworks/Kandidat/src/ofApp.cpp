#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup() {
  ofSetCircleResolution(50);
  ofSetFrameRate(100);
  theCircle.set(ofGetWidth() / 2.f, ofGetHeight() / 2.f);
  receiver.setup(OSC_PORT);
  v1.set(1.9f, 1.9f);
  ofSetBackgroundAuto(false);
}

//--------------------------------------------------------------
void ofApp::update() {
  while (receiver.hasWaitingMessages()) {
    ofxOscMessage message;
    receiver.getNextMessage(&message);
    if (message.getAddress() == "/filter") {
      v1 = v1.getRotated(message.getArgAsFloat(0) * 360.f);
      theCircle += v1;
      if (theCircle.x > ofGetWidth())
        theCircle.x = 0;
      else if (theCircle.x < 0)
        theCircle.x = ofGetWidth();
      if (theCircle.y > ofGetHeight())
        theCircle.y = 0;
      else if (theCircle.y < 0)
        theCircle.y = ofGetHeight();
    }
  }
}

//--------------------------------------------------------------
void ofApp::draw() {
  ofEnableAlphaBlending();
  ofFill();
  ofSetColor(30, 0, 30, 100);
  ofDrawCircle(theCircle.x, theCircle.y, 2);
  // ofDisableAlphaBlending();
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
