def manhattan_distance_via_b(a: tuple, b: tuple, c: tuple) -> int:
    return abs(a[0]-b[0]) + abs(a[1]-b[1]) + abs(c[0]-b[0]) + abs(c[1]-b[1])