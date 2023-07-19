class Point:
    MAX_COORD = 100
    MIN_COORD = 0


pt = Point()
print(pt.MAX_COORD, pt.MIN_COORD)

A = type('Point', (), {})
