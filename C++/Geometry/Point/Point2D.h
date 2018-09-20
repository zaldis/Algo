#pragma once
#include "stdafx.h"
#include "Edge.h"

class Point2D {
public:
	double x, y;
	Point2D(double _x = 0.0, double _y = 0.0);
	Point2D operator+ (Point2D);
	Point2D operator- (Point2D);
	friend Point2D operator* (double, Point2D);
	double operator[] (char);
	int operator== (Point2D);
	int operator!= (Point2D&);
	int operator< (Point2D&);
	int operator> (Point2D&);
	int classify(Point2D&, Point2D&);
	// int classify(Edge&);
	double polarAngle(void);
	double length(void);
	double distance(Edge&);

	enum {
		LEFT, RIGHT, BEYOND, BEHIND, BETWEEN, ORIGIN, DESTINATION
	};
};

int orientation(Point2D& p1, Point2D& p2, Point2D& p3);