#include <iostream>
#include <vector>


struct Point2D {
    double x=0, y=0;
};

struct Vector2D {
    double x=0, y=0;
};

struct Vector3D {
    double x=0, y=0, z=0;
};    

Vector3D vectorMultiple2D(Vector2D vectorA, Vector2D vectorB) {
    Vector3D result;
    result.x = 0;
    result.y = 0;
    result.z = vectorA.x * vectorB.y - vectorA.y * vectorB.x;

    return result;
}

bool collenear2D(Point2D pointA, Point2D pointB, Point2D basePoint) {
    /*
    Check if the points lie on one line
    */

    // (p1-p0) x (p2-p0) == 0
    Vector2D vectorA = { pointA.x - basePoint.x, pointA.y - basePoint.y };
    Vector2D vectorB = { pointB.x - basePoint.x, pointB.y - basePoint.y };
    Vector3D result = vectorMultiple2D(vectorA, vectorB);
    return result.z == 0;
}

double distance2D(Point2D pointA, Point2D pointB) {
    /*
    Calculate distnce between two points
    */
    double result = std::sqrt(std::pow(pointA.x - pointB.x, 2) + std::pow(pointA.y - pointB.y, 2));
    return result;
}

double leftTurn(Point2D pointA, Point2D pointB, Point2D basePoint) {
    /*
    Predicate "Left turn"
    */
    double result = (pointA.x - basePoint.x)*(pointB.y - basePoint.y) 
                  - (pointA.y - basePoint.y)*(pointB.x - basePoint.x);

    return result;
}

bool smallerAngle2D(Point2D pointA, Point2D pointB, Point2D basePoint) {
    /*
    Comparator for sorting points
    */
    if (collenear2D(pointA, pointB, basePoint)) {
        return (distance2D(pointA, basePoint) <= distance2D(pointB, basePoint));
    }

    if (leftTurn(pointA, pointB, basePoint) > 0) {
        return true;
    }

    return false;
}

std::vector<Point2D> sortCCW(std::vector<Point2D> points, int numberOfBasePoint) {
    // CCW - counterclockwise

    // Bubble Sort
    for (int i = 0; i < points.size() - 1; ++i) {
        for (int j = i + 1; j < points.size(); ++j) {
            if (!smallerAngle2D(points[i], points[j], points[numberOfBasePoint])) {
                std::swap(points[i], points[j]);
            }
        }
    }

    return points;
}



void validateVectorMultiple2D() {
    // #1
    /*Vector2D vectorA = { 1, 2 };
    Vector2D vectorB = { 2, 4 };
    Vector3D res = vectorMultiple2D(vectorA, vectorB);
    std::cout << "(1, 2)X(2, 4) = " << "(" << res.x << ", " << res.y << ", " << res.z << ");";
    std::cout << std::endl;*/

    // #2
    Vector2D vectorA = { 1, 2 };
    Vector2D vectorB = { 2, 7 };
    Vector3D res = vectorMultiple2D(vectorA, vectorB);
    std::cout << "(1, 2)X(2, 7) = " << "(" << res.x << ", " << res.y << ", " << res.z << ");";
    std::cout << std::endl;
}

void validateCollenear2D() {
    // #1
    /*Point2D a = { 1, 2 };
    Point2D b = { 2, 4 };
    Point2D base = { 4, 8 };*/


    // #2
    /*Point2D a = { 1, 2 };
    Point2D b = { 2, 4 };
    Point2D base = { 5, 8 };*/


    // #3
    Point2D a = { 1, 2 };
    Point2D b = { 1, 2 };
    Point2D base = { 1, 2 };


    if (collenear2D(a, b, base)) {
        std::cout << "Collenear" << std::endl;
    }
    else {
        std::cout << "Is not collenear" << std::endl;
    }

}

void validateSortCCW() {
    Point2D a = { 0, 0 };
    Point2D b = { 1, 1 };
    Point2D c = { 5, 6 };
    Point2D d = { 1, 3 };
    Point2D e = { 6, 5 };

    std::vector<Point2D> points = { a, d, b, c, e };
    std::vector<Point2D> res = sortCCW(points, 0);

    for (Point2D point : res) {
        std::cout << "x=" << point.x << "; y=" << point.y << ";" << std::endl;
    }
}

int main() {
    // validateVectorMultiple2D();
    // validateCollenear2D();
    // validateSortCCW();

    return 0;
}
