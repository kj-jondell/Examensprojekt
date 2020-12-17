#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup() {
  ofSetCircleResolution(50);
  ofSetFrameRate(100);
  // previousPoint.set(theCircle);
  receiver.setup(OSC_PORT);
  // points.push_back(theCircle);
  // velocity.normalize();
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
        dataThread.setReceivedData(values);
        dataThread.startThread();
      }
  }
  if (isDataReceived) {
    // std::cout << values.size() << std::endl;
    // std::cout << times.size() << std::endl;
    // points.insert(points.begin(), theCircle);
    // while (points.size() > LINE_SEGMENTS)
    //  points.pop_back();
  }
  // std::cout << dataThread.getPoints().size() << std::endl;
  // velocity = velocity.getRotated(message.getArgAsFloat(0) * 10.f);
  // theCircle += velocity;
  // if (theCircle.x > ofGetWidth() + 10) {
  //   theCircle.x = 0;
  //   points.insert(points.begin(), theCircle);
  //   // previousPoint.set(theCircle);

  // } else if (theCircle.x < -10) {
  //   theCircle.x = ofGetWidth();
  //   points.insert(points.begin(), theCircle);
  //   // previousPoint.set(theCircle);
  // }
  // if (theCircle.y > ofGetHeight() + 10) {
  //   theCircle.y = 0;
  //   points.insert(points.begin(), theCircle);
  //   // previousPoint.set(theCircle);

  // } else if (theCircle.y < -10) {
  //   theCircle.y = ofGetHeight();
  //   points.insert(points.begin(), theCircle);
  //   // previousPoint.set(theCircle);
  // }
}

//--------------------------------------------------------------
void ofApp::draw() {
  ofEnableAlphaBlending();
  ofFill();
  points = dataThread.getPoints();
  dataThread.lock();
  for (size_t i = 0; i < points.size() - 1; i++) {
    ofSetColor(255, 255, 255, ofMap(i, 0, LINE_SEGMENTS, 255, 0, true));
    // ofVec2f currentPoint = points[i + 1], lastPoint = points[i];
    // // std::cout << points[i + 1] << std::endl;
    // if (currentPoint.distance(lastPoint) <
    //     (MIN(ofGetWidth(), ofGetHeight()) - 50))
    //   ofDrawLine(currentPoint, lastPoint);
  }
  dataThread.unlock();
  // std::cout << (MIN(ofGetWidth(), ofGetHeight()) - 10) << std::endl;
  // std::cout << ofGetHeight() << std::endl;

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
// void ofApp::exit() { dataThread.stopThread(); }
