#pragma once

#include "Point2D.h"

class Edge {
	Point2D org;
	Point2D dest;
	Edge(Point2D& _org, Point2D& _dest);
	Edge(void);
	Edge& rot(void);
	Edge& flip(void);
	Point2D point(double);
	int intersect(Edge&, double&);
	int cross(Edge&, double&);
	bool isVertical(void);
	double slope(void);
	double y(double);

	enum {
		COLLINEAR, PARALLEL, SKEW, SKEW_CROSS, SKEW_NO_CROSS
	};
};