import math
import sys


def calculate_point_distance(x, y, n, m):
    distance = math.sqrt((x - n) ** 2 + (y - m) ** 2)
    return distance


def yield_special_fields(fields):
    for f in fields:
        yield f


def all_fields(n, m):
    ret = []
    for i in range(0, n):
        for j in range(0, m):
            yield (i, j, -1, sys.maxsize)


def find_min_distance(n, m, num_fields):

    all_fields_arr = all_fields(n, m)

    for f in all_fields_arr:
        n, m, index, distance = f
        for spec in yield_special_fields(num_fields):
            x, y, i = spec
            d = calculate_point_distance(x, y, n, m)
            if d < distance:
                distance = d
                index = i
            ret = index

        yield ret





