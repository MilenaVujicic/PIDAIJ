import math
import multiprocessing as mp
import tracemalloc

def number_generator(num):
    return num

def is_prime(a):
    flag = True
    for b in range(2, math.floor(math.sqrt(a))+1):
        if a%b == 0:
            flag = False

    return flag

def prime_number(num):
    if is_prime(num):
        return num
    else:
        return None        

def prime_to_hex(num):
    if is_prime(num):
        return hex(num)
    else:
        return None

def hex_dictionary(arr):
    ret_dict = {}

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
  
    arr = []
    print("The hexadecimal values are: ")
    with mp.Pool(mp.cpu_count()) as pool:
        r = pool.imap(prime_to_hex, range(1,n))
        for num in r:
            if num is not None:
                print(num)
                arr.append(num)

        hexdict = hex_dictionary(arr)
        print("Hexadecimal dictionary is, ", hexdict)
        current, peak = tracemalloc.get_traced_memory()
        print(f"Current memory usage is {current / 10**6}MB; Peak was {peak / 10**6}MB")
        tracemalloc.stop()



if __name__=="__main__":
    main()


    