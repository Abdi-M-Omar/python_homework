# --------------------------------------------------
# Task 5: Extending a Class
# --------------------------------------------------

import math


# Represents a point in two-dimensional space.
class Point:

    # Store the x and y coordinates.
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Return True when two points have the same coordinates.
    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    # Return a readable string representation of the point.
    def __str__(self):
        return f"Point({self.x}, {self.y})"

    # Calculate the Euclidean distance to another point.
    def distance(self, other):
        x_difference = other.x - self.x
        y_difference = other.y - self.y

        return math.sqrt(
            x_difference ** 2 + y_difference ** 2
        )


# Vector inherits the x and y coordinates and equality method from Point.
class Vector(Point):

    # Override the string representation.
    def __str__(self):
        return f"Vector({self.x}, {self.y})"

    # Override the + operator to perform vector addition.
    def __add__(self, other):
        return Vector(
            self.x + other.x,
            self.y + other.y
        )


# --------------------------------------------------
# Demonstrate the Point class
# --------------------------------------------------

point1 = Point(1, 2)
point2 = Point(4, 6)
point3 = Point(1, 2)

print(point1)
print(point2)

print(point1 == point2)   # False
print(point1 == point3)   # True

print(point1.distance(point2))   # 5.0


# --------------------------------------------------
# Demonstrate the Vector class
# --------------------------------------------------

vector1 = Vector(2, 3)
vector2 = Vector(4, 5)

print(vector1)
print(vector2)

vector3 = vector1 + vector2

print(vector3)   # Vector(6, 8)