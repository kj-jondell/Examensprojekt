#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup() {
  ofSetCircleResolution(50);
  ofSetFrameRate(100);
  theCircle.set(ofGetWidth() / 2.f, ofGetHeight() / 2.f);
  previousPoint.set(theCircle);
  receiver.setup(OSC_PORT);
  velocity.set(5.0f, 5.0f);
  // velocity.normalize();
  ofSetBackgroundAuto(false);
}

//--------------------------------------------------------------
void ofApp::update() {
  while (receiver.hasWaitingMessages()) {
    ofxOscMessage message;
    receiver.getNextMessage(&message);
    if (message.getAddress() == "/filter") {
      velocity = velocity.getRotated(message.getArgAsFloat(0) * 10.f);
      theCircle += velocity;
      if (theCircle.x > ofGetWidth()) {
        theCircle.x = 0;
        previousPoint.set(theCircle);

      } else if (theCircle.x < 0) {
        theCircle.x = ofGetWidth();
        previousPoint.set(theCircle);
      }
      if (theCircle.y > ofGetHeight()) {
        theCircle.y = 0;
        previousPoint.set(theCircle);

      } else if (theCircle.y < 0) {
        theCircle.y = ofGetHeight();
        previousPoint.set(theCircle);
      }
    }
  }
}

//--------------------------------------------------------------
void ofApp::draw() {
  ofEnableAlphaBlending();
  ofFill();
  ofSetColor(90, 89, 99, 100);
  ofDrawLine(theCircle, previousPoint);
  previousPoint.set(theCircle);
  // ofDrawCircle(theCircle.x, theCircle.y, 2);
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
