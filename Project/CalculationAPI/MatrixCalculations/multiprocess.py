import multiprocessing as mp
import math
import sys


def calculate_point_distance(x, y, n, m):
    distance = math.sqrt((x - n) ** 2 + (y - m) ** 2)
    return distance


def matrix_array(n, m, fields):
    cnt = -1
    for i in range(n):
        for j in range(m):
            distance = sys.maxsize
            ret_cnt = -1
            for f in fields:
                x, y, dist = f
                if x == i and y == j:
                    distance = 0
                    cnt += 1
                    ret_cnt = cnt

            yield i, j, distance, ret_cnt


def calculate_distance(matrix):
    for m1 in matrix:
        i1, j1, d1, ind1 = m1
        if d1 == 0:
            yield ind1
        else:
            for m2 in matrix:
                i2, j2, d2, ind2 = m2
                if d2 == 0:
                    dist = calculate_point_distance(i1, j1, i2, j2)
                    if dist < d1:
                        d1 = dist
                        ret_id = ind2
                ret = ret_id
            yield ret


def parallelize(n, m, fields):
    n_cpu = mp.cpu_count()
    k = len(fields)
    it = matrix_array(n, m, fields)
    with mp.Pool(n_cpu) as pool:
        r = pool.imap(calculate_distance, next(it))
        for num in r:
            yield num