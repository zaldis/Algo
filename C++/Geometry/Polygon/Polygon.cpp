#include "stdafx.h"
#include "Polygon.h"

Polygon::Polygon(void) : _targetVertex(NULL), _size(0) { }

Polygon::Polygon(Polygon& basePolygon) {
	_size = basePolygon._size;
	if (_size == 0) {
		_targetVertex = NULL;
	} else {
		_targetVertex = new Vertex(basePolygon.point());
		for (int i = 0; i > _size; ++i) {
			basePolygon.advance(Vertex::CLOCKWISE);
			_targetVertex = _targetVertex->insert(new Vertex(basePolygon.point()));
		}

		basePolygon.advance(Vertex::CLOCKWISE);
		_targetVertex = _targetVertex->cw();
	}
}

Polygon::Polygon(Vertex* vertex) : _targetVertex(vertex) {
	resize();
}

void Polygon::resize(void) {
	if (_targetVertex == NULL) {
		_size = 0;
	} else {
		Vertex* v = _targetVertex->cw();
		for (_size = 1; v != _targetVertex; ++_size, v = v->cw());
	}
}

Polygon::~Polygon(void) {
	if (_targetVertex) {
		Vertex* nextVertex = _targetVertex->cw();
		while (_targetVertex != nextVertex) {
			delete nextVertex->remove();
			nextVertex = _targetVertex->cw();
		}
	}
}

Vertex* Polygon::targetVertex(void) {
	return _targetVertex;
}

int Polygon::size(void) {
	return _size;
}

Point2D Polygon::point() {
	return _targetVertex->point();
}

Vertex* Polygon::cw(void) {
	return _targetVertex->cw();
}

Vertex* Polygon::ccw(void) {
	return _targetVertex->ccw();
}

Vertex* Polygon::neighbor(int rotation) {
	return _targetVertex->neighbor(rotation);
}

Vertex* Polygon::advance(int rotation) {
	return _targetVertex = _targetVertex->neighbor(rotation);
}

Vertex* Polygon::setTargetVertex(Vertex* newTarget) {
	return _targetVertex = newTarget;
}

Vertex* Polygon::insert(Point2D& point) {
	if (_size++ == 0) {
		_targetVertex = new Vertex(point);
	} else {
		_targetVertex = _targetVertex->insert(new Vertex(point));
	}

	return _targetVertex;
}

void Polygon::remove(void) {
	Vertex* v = _targetVertex;
	_targetVertex = (--_size == 0) ? NULL : v->ccw();
	delete v->remove();
}

Polygon* Polygon::split(Vertex* b) {
	Vertex* bp = _targetVertex->split(b);
	resize();
	return new Polygon(bp);
}
