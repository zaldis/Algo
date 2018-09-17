#include "stdafx.h"

#include "Point2D.h"
#include <cmath>

Point2D::Point2D(double _x, double _y): x(_x), y(_y) { }

Point2D Point2D::operator+(Point2D& point) {
	return Point2D(x + point.x, y + point.y);
}

Point2D Point2D::operator-(Point2D& point) {
	return Point2D(x - point.x, y - point.y);
}

Point2D operator*(double value, Point2D& point) {
	return Point2D(value * point.x, value * point.y);
}

double Point2D::operator[] (char coordName) {
	switch (coordName) {
	case 'x':
		return x;
	case 'y':
		return y;
	default:
		return 0.0;
	}
}

int Point2D::operator== (Point2D& point) {
	return (x == point.x) && (y == point.y);
}

int Point2D::operator!= (Point2D& point) {
	return !(*this == point);
}

int Point2D::operator< (Point2D& point) {
	return ((x < point.x) || ((x == point.x) && y < point.y));
}

int Point2D::operator> (Point2D& point) {
	return ((x > point.x) || ((x == point.x) && (y > point.y)));
}

int orientation(Point2D& p0, Point2D& p1, Point2D& p2) {
	Point2D a = p1 - p0;
	Point2D b = p2 - p0;
	double sa = a.x * b.y - b.x * a.y;

	if (sa > 0.0)
		return 1;
	if (sa < 0.0)
		return -1;
	return 0;
}

enum {
	LEFT, RIGHT, BEYOND, BEHIND, BETWEEN, ORIGIN, DESTINATION
};

int Point2D::classify(Point2D& p0, Point2D& p1) {
	Point2D p2 = *this;
	Point2D a = p1 - p0;
	Point2D b = p2 - p0;
	double sa = a.x * b.y - a.y * b.x;

	if (sa > 0.0)
		return LEFT;
	if (sa < 0.0)
		return RIGHT;
	if ((a.x * b.x < 0.0) || (a.y * b.y < 0.0))
		return BEHIND;
	if (a.length() < b.length())
		return BEYOND;
	if (p0 == p2)
		return ORIGIN;
	if (p1 == p2)
		return DESTINATION;

	return BETWEEN;
}

double Point2D::polarAngle(void) {
	if ((x == 0.0) && (y == 0.0)) {
		return -1.0;
	}

	if (x == 0.0)
		return ((y > 0.0) ? 90 : 270);

	double theta = atan(y / x);
	const double PI = 3.1415926;
	theta *= 360 / (2 * PI);

	if (x > 0.0)
		return ((y >= 0.0) ? theta : 360 + theta);
	else
		return 180 + theta;
}

double Point2D::length() {
	return std::sqrt(x*x + y*y);
}