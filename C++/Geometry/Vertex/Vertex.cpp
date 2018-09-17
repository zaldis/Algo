#include "stdafx.h"
#include "Vertex.h"

Vertex::Vertex(double x, double y) : Point2D(x, y) { }

Vertex::Vertex(Point2D point) : Point2D(point) { }

Vertex* Vertex::cw(void) {
	return (Vertex*)_next;
}

Vertex* Vertex::ccw(void) {
	return (Vertex*)_prev;
}

Vertex* Vertex::neighbor(int rotation) {
	return (rotation == Rotation::CLOCKWISE) ? cw() : ccw();
}

Point2D Vertex::point() {
	return *((Point2D*) this);
}

Vertex* Vertex::insert(Vertex* vertex) {
	return (Vertex*)(Node::insert(vertex));
}

Vertex* Vertex::remove(void) {
	return (Vertex*)(Node::remove());
}

void Vertex::splice(Vertex* vertex) {
	Node::splice(vertex);
}

Vertex* Vertex::split(Vertex* b) {
	Vertex* bp = b->ccw()->insert(new Vertex(b->point()));
	insert(new Vertex(point()));

	splice(bp);
	return bp;
}