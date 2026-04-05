from point2d import Point2D

p1 = Point2D(3, 4)  # dist=5.0
p2 = Point2D(0, 0)  # dist=0.0
p3 = Point2D(5, 12) # dist=13.0

print(p2 < p1)   # True (0 < 5)
print(p1 < p3)   # True (5 < 13)
print(p1 == Point2D(3, 4))  # True
print(p1 != p2)  # True
print(p3 >= p1)  # True
print(p1)

