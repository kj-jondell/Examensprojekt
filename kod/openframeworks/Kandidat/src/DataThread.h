#include "ofMain.h"
#include "ofMath.h"
#include "ofThread.h"
#include "ofTimer.h"
#include <vector>

#define SLEEP_TIME 20

class DataThread : public ofThread {

public:
  std::vector<ofVec2f> getPoints() { return this->points; }
  void setReceivedData(std::vector<float> data) { receivedData = data; }

private:
  std::vector<ofVec2f> points;
  std::vector<float> receivedData = {};
  ofVec2f theCircle, velocity;

  void threadedFunction() {
    // theCircle.set(ofGetWidth() / 2.f, ofGetHeight() / 2.f);
    // velocity.set(5.0f, 5.0f);
    // int index = 0;

    // while (isThreadRunning()) {
    //  if (receivedData.size() > 0) {
    //    lock();
    //    velocity = velocity.getRotated(receivedData[index++] * 10.f);
    //    theCircle += velocity;
    //    if (theCircle.x > ofGetWidth() + 10) {
    //      theCircle.x = 0;
    //      points.insert(points.begin(), theCircle);
    //      // previousPoint.set(theCircle);

    //    } else if (theCircle.x < -10) {
    //      theCircle.x = ofGetWidth();
    //      points.insert(points.begin(), theCircle);
    //      // previousPoint.set(theCircle);
    //    }
    //    if (theCircle.y > ofGetHeight() + 10) {
    //      theCircle.y = 0;
    //      points.insert(points.begin(), theCircle);
    //      // previousPoint.set(theCircle);

    //    } else if (theCircle.y < -10) {
    //      theCircle.y = ofGetHeight();
    //      points.insert(points.begin(), theCircle);
    //      // previousPoint.set(theCircle);
    //    }
    //    while (points.size() > LINE_SEGMENTS)
    //      points.pop_back();
    //    unlock();
    //    sleep(SLEEP_TIME);
    //  }
    //}
  }
};
