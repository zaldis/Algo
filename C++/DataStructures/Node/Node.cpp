#include "stdafx.h"
#include "Node.h"

Node::Node(void) : _next(this), _prev(this) { }

Node::~Node(void) { }

Node* Node::next() {
	return _next;
}

Node* Node::prev() {
	return _prev;
}

Node* Node::insert(Node* newNode) {
	Node* next = _next;
	newNode->_next = next;
	newNode->_prev = this;
	_next = newNode;
	_next->_prev = newNode;

	return newNode;
}

Node* Node::remove(void) {
	_prev->_next = _next;
	_next->_prev = _prev;
	_next = _prev = this;

	return this;
}

void Node::splice(Node* node) {
	Node* a = this;
	Node* aNext = a->_next;
	Node* nodeNext = node->_next;

	a->_next = nodeNext;
	node->_next = aNext;
	aNext->_prev = node;
	nodeNext->_prev = a;
}