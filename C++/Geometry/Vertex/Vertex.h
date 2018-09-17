#pragma once

#include "Node.h"
#include "Point2D.h"

class Vertex: public Node, public Point2D {
public:
	Vertex(double x, double y);
	Vertex(Point2D);
	Vertex* cw(void);
	Vertex* ccw(void);
	Vertex* neighbor(int rotation);
	Point2D point(void);
	Vertex* insert(Vertex*);
	Vertex* remove(void);
	void splice(Vertex*);
	Vertex* split(Vertex*);

	enum Rotation {
		CLOCKWISE, COUNTER_CLOCKWISE
	};

	friend class Polygon;
};
