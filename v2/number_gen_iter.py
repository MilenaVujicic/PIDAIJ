import math
import tracemalloc

def number_generator(n):
    for arr in range(1, n+1):
        yield arr

def is_prime(a):
    flag = True
    for b in range(2, math.floor(math.sqrt(a))+1):
        if a%b == 0:
            flag = False

    return flag

def prime_number(n):
    arr = number_generator(n)
    for a in arr:
        if is_prime(a):
            yield a


def prime_to_hex(arr):
    ret_arr = [hex(a) for a in arr]
    return ret_arr

def prime_to_hex_yield(n):
    for i in prime_number(n):
        yield hex(i)


def hex_dictionary(n):
    ret_dict = {}
    arr = prime_to_hex_yield(n)

    for a in arr:
        for char in a[2:]:
            if char in ret_dict.keys():
                ret_dict[char] += 1
            else:
                ret_dict[char] = 1
    return ret_dict

        

def main():
    try:
        n = int(input("Enter array size "))
    except Exception:
        print("Input wasn't a number")
    tracemalloc.start()

    arr = hex_dictionary(n)
    print(arr)
    current, peak = tracemalloc.get_traced_memory()
    print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
    tracemalloc.stop()


if __name__=="__main__":
    main()


    
