# Week2 - OF project

Chang Wang 20036997

<br />

Let's start by looking at the results.

![](https://static.wixstatic.com/media/27541e_a98cf2f3059b42de9e79e874b7d279d8~mv2.gif)


The first effect I'm going to make is that the eyes of the two little animals above will change as the mouse position changes, which I think still looks interesting. 

Suppose the coordinates of the centre of the eye frame are A(x,y) and the coordinates of the mouse are B(xm,ym), find the magnitude of the angle α between the two points of AB and the x-axis (actually in openframework it is not the x-axis, it is at the top left corner of the window as the origin, horizontally to the right as the x-axis and vertically down as the y-axis). This angle is then used to calculate the coordinates of the centre of the eye, E, using the size of this angle, the radius of the orbit, R, and the coordinates of the centre of the eye, A. This allows the eye to move with the mouse. In addition I have added another judgement statement that if the distance between the coordinates of the mouse and the eye socket is less than the radius of the eye socket, the position of the eye will be the position of the mouse.

To make the image look more interesting, I added the two little balls from the example in openframework, which also change shape with the mouse coordinates.

<br />

## Code section.

### main.cpp

Here I just change the initial window size.
````C++
//main.cpp
#include "ofMain.h"
#include "ofApp.h"


int main() {
	ofSetupOpenGL(640, 640, OF_WINDOW);

	// this kicks off the running of my app
	// can be OF_WINDOW or OF_FULLSCREEN
	// pass in width and height too:
	ofRunApp(new ofApp());

}
````

<br />

### ofApp.h

There are only a few variables defined here, so much of the previous code is self-contained, only the following variable definition statements are the ones I changed.

````C++
#pragma once

#include "ofMain.h"

class ofApp : public ofBaseApp{

	public:
		void setup();
		void update();
		void draw();

		void keyPressed(int key);
		void keyReleased(int key);
		void mouseMoved(int x, int y );
		void mouseDragged(int x, int y, int button);
		void mousePressed(int x, int y, int button);
		void mouseReleased(int x, int y, int button);
		void mouseEntered(int x, int y);
		void mouseExited(int x, int y);
		void windowResized(int w, int h);
		void dragEvent(ofDragInfo dragInfo);
		void gotMessage(ofMessage msg);
		

		ofImage img;
		float pi = 3.1415;
		float jd[4];
		float z[4],z1;

};
````

<br />

### ofApp.cpp

Here is a concrete implementation of the draw eye function.

````c++
#include "ofApp.h"

//--------------------------------------------------------------
void ofApp::setup(){
	ofSetVerticalSync(true);
	img.load("indispensable.jpg");
	
}

//--------------------------------------------------------------
void ofApp::update(){

}

//--------------------------------------------------------------
void ofApp::draw(){

	ofBackground(ofColor::black);

	// draw the original image
	ofSetColor(ofColor::white);
	img.draw(60,60);
	ofSetColor(ofColor::black);
	float xP = (float)(mouseX)-60;
	float yP = (float)(mouseY)-60;
	float xPct1 = (float)(mouseX);
	float yPct1 = (float)(mouseY);

	ofFill();		// draw "filled shapes"
	
	float X[4] = {209,264,105,376};
	float Y[4] = {144,146,389,392};
	float x[4], y[4];
	float R,r;
	for (int i = 0; i < 4; i++)
	{
		//if
		z[i] = sqrt(((yP - Y[i])*(yP - Y[i]) +(xP - X[i])*(xP - X[i])));

		jd[i] =asin( (xP - X[i])/z[i]);
		z1=asin((xP - X[i]) / z[i]);

		if (yP < Y[i])
			jd[i] = pi - jd[i];
	
		if (i < 2)
		{
			R = 17.5;
			r = 5;
			x[i] = X[i] + R * sin(jd[i]);
			y[i] = Y[i] + R * cos(jd[i]);
			if (z[i] < 20)
				ofDrawCircle(xPct1, yPct1, r);
			else
			ofDrawCircle(x[i] + 60, y[i] + 60, r);
		}
		else 
		{
			R = 55; 
			r = 20;
			x[i] = X[i] + R * sin(jd[i]);
		    y[i] = Y[i] + R * cos(jd[i]);
			if(z[i]<60)
				ofDrawCircle(xPct1,yPct1 ,r);
			else
		    ofDrawCircle(x[i]+60, y[i]+60, r);
		}
		
	}





	float xPct = (float)(mouseX) / (float)(ofGetWidth());
	float yPct = (float)(mouseY) / (float)(ofGetHeight());
	int nTips = 5 + xPct * 30;
	int nStarPts = nTips * 2;
	float angleChangePerPt = TWO_PI / (float)nStarPts;
	float innerRadius = 0 + yPct * 40;
	float outerRadius = 40;
	float origx = 400;
	float origy = 120;
	float angle = 0;

	ofSetHexColor(0xa16bca);
	ofBeginShape();
	for (int i = 0; i < nStarPts; i++) {
		if (i % 2 == 0) {
			// inside point:
			float x = origx + innerRadius * cos(angle);
			float y = origy + innerRadius * sin(angle);
			ofVertex(x, y);
		}
		else {
			// outside point
			float x = origx + outerRadius * cos(angle);
			float y = origy + outerRadius * sin(angle);
			ofVertex(x, y);
		}
		angle += angleChangePerPt;
	}
	ofEndShape();

	ofSetColor(ofColor::turquoise);

	ofBeginShape();

	int nTips1 = 5 + xPct * 30;
	int nStarPts1= nTips1 * 2;
	float angleChangePerPt1= TWO_PI / (float)nStarPts1;
	float innerRadius1 = 0 + yPct * 25;
	float outerRadius1 = 25;
	float origx1 = 192;
	float origy1 = 173;
	float angle1 = 0;

	for (int i = 0; i < nStarPts1; i++) 
	{
		if (i % 2 == 0) {
			// inside point:
			float x1 = origx1 + innerRadius1 * cos(angle1);
			float y1 = origy1 + innerRadius1 * sin(angle1);
			ofVertex(x1, y1);
		}
		else {
			// outside point
			float x1 = origx1 + outerRadius1 * cos(angle1);
			float y1 = origy1 + outerRadius1 * sin(angle1);
			ofVertex(x1, y1);
		}
		angle1 += angleChangePerPt1;
	}

	ofEndShape();
}

//--------------------------------------------------------------
void ofApp::keyPressed(int key){

}

//--------------------------------------------------------------
void ofApp::keyReleased(int key){

}

//--------------------------------------------------------------
void ofApp::mouseMoved(int x, int y ){

}

//--------------------------------------------------------------
void ofApp::mouseDragged(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mousePressed(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseReleased(int x, int y, int button){

}

//--------------------------------------------------------------
void ofApp::mouseEntered(int x, int y){

}

//--------------------------------------------------------------
void ofApp::mouseExited(int x, int y){

}

//--------------------------------------------------------------
void ofApp::windowResized(int w, int h){

}

//--------------------------------------------------------------
void ofApp::gotMessage(ofMessage msg){

}

//--------------------------------------------------------------
void ofApp::dragEvent(ofDragInfo dragInfo){ 

}
````

<br />

One of the disadvantages of the implementation is that if the size of "yP" and "Y[i]" is not judged, the angle jd[i] will only be in the range of (0, π), which will cause the eyes of those two small animals to turn only within 0~180°, which will look awkward.











