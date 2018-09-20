#include "stdafx.h"

#include "Edge.h"
#include "Point2D.h"
#include <limits>

Edge::Edge(Point2D* _org, Point2D* _dest) : org( _org), dest(_dest) { }

Edge::Edge(void) : org(new Point2D(0, 0)), dest(new Point2D(0, 0)) { }

Edge::Edge(Edge& edge) {
	if (org)
		delete org;
	if (dest)
		delete dest;

	this->org = new Point2D(*(edge.org));
	this->dest = new Point2D(*(edge.dest));
}

Edge& Edge::rot(void) {
	Point2D middlePoint = 0.5 * (*dest + *org);
	Point2D vector = *dest - *org;
	Point2D normal = Point2D(vector.y, -vector.x);
	delete org;
	delete dest;
	org = new Point2D(middlePoint - 0.5 * normal);
	dest = new Point2D(middlePoint + 0.5 * normal);

	return *this;
}

Edge& Edge::flip(void) {
	return rot().rot();
}

Point2D* Edge::point(double t) {
	return new Point2D(*org + t * (*dest - *org));
}

double dotProduct(Point2D& pointA, Point2D pointB) {
	return pointA.x * pointB.x + pointA.y * pointB.y;
}

int Edge::intersect(Edge& edge, double& t) {
	Point2D a = *org;
	Point2D b = *dest;
	Point2D c = *(edge.org);
	Point2D d = *(edge.dest);

	Point2D normal = Point2D((d - c).y, (c - d).x);
	double scalar = dotProduct(normal, b - a);
	if (scalar == 0.0) {
		int type = a.classify(*(edge.org), *(edge.dest));
		if (type == Point2D::LEFT || type == Point2D::RIGHT) {
			return PARALLEL;
		} else {
			return COLLINEAR;
		}
	}

	double num = dotProduct(normal, a - c);
	t = -num / scalar;
	return SKEW;
}

int Edge::cross(Edge& edge, double& t) {
	double s;
	int crossType = edge.intersect(*this, s);
	if ((crossType == COLLINEAR) || (crossType == PARALLEL))
		return crossType;

	if ((s < 0.0) || (s > 1.0)) {
		return SKEW_NO_CROSS;
	}
	intersect(edge, t);
	if ((0.0 <= t) && (t <= 1.0))
		return SKEW_CROSS;
	else
		return SKEW_NO_CROSS;
}

bool Edge::isVertical(void) {
	return ((*org).x == (*dest).x);
}

double Edge::slope(void) {
	if (!isVertical())
		return (dest->y - org->y) / (dest->x - org->x);

	return std::numeric_limits<double>::infinity();
}

double Edge::y(double x) {
	return slope() * (x - org->x) + org->y;
}

Edge& Edge::operator= (Edge& edge) {
	if (org)
		delete org;
	if (dest)
		delete dest;

	this->org = new Point2D(*(edge.org));
	this->dest = new Point2D(*(edge.dest));

	return *this;
}