import math

def number_generator(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    
    return arr

def prime_number(arr):
    length = len(arr)
    flag = True
    ret_arr = []

    for a in range(2, length+1):
        for b in range(2, math.floor(math.sqrt(a))+1):
            if a%b == 0:
                flag = False
        if flag == True:
            ret_arr.append(a)
        flag = True        
                
    return ret_arr

try:
    n = int(input("Enter array size "))
except Exception:
    print("Input wasn't a number")
    
arr = number_generator(n)
print("The array is ", arr)
print("The primes are ", prime_number(arr))
print(len(prime_number(arr)))