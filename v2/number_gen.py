import math

def number_generator(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    
    return arr

def is_prime(a):
    flag = True
    for b in range(2, math.floor(math.sqrt(a))+1):
        if a%b == 0:
            flag = False

    return flag

def prime_number(arr):
    length = len(arr)

    ret_arr = []

    for a in range(2, length+1):
        if is_prime(a):
            ret_arr.append(a)     
                
    return ret_arr

def prime_to_hex(arr):
    ret_arr = []
    for a in arr:
        ret_arr.append(hex(a))

    return ret_arr

try:
    n = int(input("Enter array size "))
except Exception:
    print("Input wasn't a number")
    
arr = number_generator(n)
primes = prime_number(arr)
hexadecimal = prime_to_hex(primes)
print("The array is ", arr)
print("The primes are ", primes)
print("Hexadecimal values are, ", hexadecimal)