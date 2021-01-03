import multiprocessing as mp
import math
import sys


special_fields = []


def calculate_fields_distance(field):
    n, m= field
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


def yield_matrix(n, m):
    for i in range(n):
        for j in range(m):
            yield (i, j)


def return_matrix(n, m):
    ret = []
    for i in range(n):
        for j in range(m):
            ret.append((i, j))
    return ret


def parallelize(n, m, fields):
    global special_fields
    init_calc(fields)
    ret_val = []
    with mp.Pool(processes=mp.cpu_count()) as pool:
        res = pool.map(calculate_fields_distance, yield_matrix(n, m))
        for r in res:
            yield r


def init_calc(spec):
    global special_fields
    for s in spec:
        special_fields.append(s)

    return special_fields