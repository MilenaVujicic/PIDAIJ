from django.http import JsonResponse
from rest_framework.parsers import JSONParser
from MatrixCalculations import sequential as seq
from MatrixCalculations import generator as gen
from MatrixCalculations import multiprocess as mp
from MatrixCalculations import comprehension as com
from django.views.decorators.csrf import csrf_exempt
import time
import tracemalloc
import json
# Create your views here.


n = 1500
m = 1500
points = ["1,3", "3,2", "6,8", "9,6", "5,5",
          "15,16", "19,19", "20,20",
          "25,27", "26,29", "30,35",
          "40,40", "70,71", "99, 100",
          "500,500", "750,851"]


'''
n = 10
m = 10
points = ["1,3", "3,2", "6,8", "9,6", "5,5"]
'''
json_data = {
    "n": n,
    "m": m,
    "points": points
}


def parse_special_fields(spec):
    ret_val = []
    i = 0
    for s in spec:
        temp = s.split(",")
        ret_val.append((int(temp[0]), int(temp[1]), i))
        i+=1
    return ret_val


@csrf_exempt
def calculate_sequential(request):
    if request.method == "GET":
        data = json_data
    elif request.method == "POST":
        data = JSONParser().parse(request)

    n = data["n"]
    m = data["m"]
    spec = data["points"]
    spec = parse_special_fields(spec)
    tracemalloc.start()
    start_t = time.time()
    result = seq.calculate_distance(n, m, spec)
    end_t = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    time_in_s = end_t-start_t
    max_memory_in_MB = peak/10**6
    ret_data = {
        "result": result,
        "time_in_s": time_in_s,
        "max_memory_in_MB": max_memory_in_MB
    }

    ret_data = json.dumps(ret_data)
    return JsonResponse(data=ret_data, status=200, safe=False)


@csrf_exempt
def calculate_generator(request):
    if request.method == "GET":
        data = json_data
    elif request.method == "POST":
        data = JSONParser().parse(request)

    result = []
    n = data["n"]
    m = data["m"]
    spec = data["points"]
    spec = parse_special_fields(spec)
    tracemalloc.start()
    start_t = time.time()
    res = gen.calculate_distance(n, m, spec)
    for r in res:
        result.append(r)
    end_t = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_in_s = end_t-start_t
    max_memory_in_MB = peak/10**6
    ret_data = {
        "result": result,
        "time_in_s": time_in_s,
        "max_memory_in_MB": max_memory_in_MB
    }
    ret_data = json.dumps(ret_data)

    return JsonResponse(data=ret_data, status=200, safe=False)


@csrf_exempt
def calculate_comprehension(request):
    if request.method == "GET":
        data = json_data
    elif request.method == "POST":
        data = JSONParser().parse(request)

    n = data["n"]
    m = data["m"]
    spec = data["points"]
    spec = parse_special_fields(spec)
    tracemalloc.start()
    start_t = time.time()
    result = com.calculate_distance(n, m, spec)
    end_t = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_in_s = end_t-start_t
    max_memory_in_MB = peak/10**6
    ret_data = {
        "result": result,
        "time_in_s": time_in_s,
        "max_memory_in_MB": max_memory_in_MB
    }
    ret_data = json.dumps(ret_data)

    return JsonResponse(data=ret_data, status=200, safe=False)



@csrf_exempt
def calculate_multiprocess(request):
    if request.method == "GET":
        data = json_data
    elif request.method == "POST":
        data = JSONParser().parse(request)

    n = data["n"]
    m = data["m"]
    spec = data["points"]
    spec = parse_special_fields(spec)
    tracemalloc.start()
    start_t = time.time()
    res = mp.parallelize(n, m, spec)
    result = []
    for r in res:
        result.append(r)
    end_t = time.time()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()
    time_in_s = end_t - start_t
    max_memory_in_MB = peak / 10 ** 6
    ret_data = {
        "result": result,
        "time_in_s": time_in_s,
        "max_memory_in_MB": max_memory_in_MB
    }
    ret_data = json.dumps(ret_data)

    return JsonResponse(data=ret_data, status=200, safe=False)