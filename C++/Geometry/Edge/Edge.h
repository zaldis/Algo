#pragma once
#include "stdafx.h"

class Point2D;

class Edge {
public:
	Point2D* org;
	Point2D* dest;
	Edge(Point2D* _org, Point2D* _dest);
	Edge(Edge&);
	Edge(void);
	Edge& rot(void);
	Edge& flip(void);
	Point2D* point(double);
	int intersect(Edge&, double&);
	int cross(Edge&, double&);
	bool isVertical(void);
	double slope(void);
	double y(double);

	Edge& operator= (Edge&);

	enum {
		COLLINEAR, PARALLEL, SKEW, SKEW_CROSS, SKEW_NO_CROSS
	};
};