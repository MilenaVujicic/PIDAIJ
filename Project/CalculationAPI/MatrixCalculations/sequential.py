import math
import sys


def calculate_point_distance(x, y, n, m):
    distance = math.sqrt((x - n) ** 2 + (y - m) ** 2)
    return distance


def all_fields(n, m):
    ret = []
    for i in range(0, n):
        for j in range(0, m):
            ret.append((i, j, -1, sys.maxsize))

    return ret


def find_min_distance(all_fields, fields):

    field_distances = []

    for f in all_fields:
        n, m, index, distance = f
        for spec in fields:
            x, y, i = spec
            d = calculate_point_distance(x, y, n, m)
            if d < distance:
                distance = d
                index = i
            ret = index

        field_distances.append(ret)

    return field_distances