import math

class Point2D:
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def _distance(self):
        return math.sqrt(self.x**2 + self.y**2)

    def __lt__(self, other):
        return self._distance() < other._distance()

    def __gt__(self, other):
        return self._distance() > other._distance()

    def __eq__(self, other):
        return self._distance() == other._distance()

    def __ne__(self, other):
        return self._distance() != other._distance()

    def __le__(self, other):
        return self._distance() <= other._distance()

    def __ge__(self, other):
        return self._distance() >= other._distance()

    def __str__(self):
        return f"Point2D({self.x}, {self.y})"

