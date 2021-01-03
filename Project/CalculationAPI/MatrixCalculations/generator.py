import math
import sys


def calculate_distance(n, m, fields):
    for i in range(n):
        for j in range(m):
            res = calculate_fields_distance((i, j), fields)
            yield res


def init_calc(spec):
    for s in spec:
        yield s


def calculate_fields_distance(field, fields):
    n, m= field
    min_dist = sys.maxsize
    idx = -1
    ret = None
    special_fields = init_calc(fields)
    for s in special_fields:
        x, y, index = s
        distance = math.sqrt((x - n) ** 2 + (y - m) ** 2)
        if distance < min_dist:
            min_dist = distance
            idx = index
        ret = idx
    return ret



