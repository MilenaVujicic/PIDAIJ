import math
import sys

special_fields = []


def calculate_fields_distance(field):
    n, m = field
    min_dist = sys.maxsize
    idx = -1
    for s in special_fields:
        x, y, index = s
        distance = math.sqrt((x - n) ** 2 + (y - m) ** 2)
        if distance < min_dist:
            min_dist = distance
            idx = index
        ret = idx
    return ret


def calculate_distance(n, m, fields):
    global special_fields
    init_calc(fields)

    res = [(calculate_fields_distance((i, j))) for i in range(n) for j in range(m)]
    return res


def init_calc(spec):
    global special_fields
    for s in spec:
        special_fields.append(s)

    return special_fields