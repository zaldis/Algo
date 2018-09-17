#pragma once

#include "Vertex.h"

class Polygon {
private:
	Vertex * _targetVertex;
	int _size;
	void resize(void);

public:
	Polygon(void);
	Polygon(Polygon&);
	Polygon(Vertex*);
	~Polygon(void);

	Vertex* targetVertex(void);
	int size(void);
	Point2D point(void);
	/*Edge edge(void);*/
	Vertex* cw(void);
	Vertex* ccw(void);
	Vertex* neighbor(int rotation);
	Vertex* advance(int rotation);
	Vertex* setTargetVertex(Vertex*);
	Vertex* insert(Point2D&);
	void remove(void);

	Polygon* split(Vertex*);
};
