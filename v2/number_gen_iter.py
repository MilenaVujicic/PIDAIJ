import math

def number_generator(n):
    arr = [i for i in range (1, n+1)]

    yield arr

def is_prime(a):
    flag = True
    for b in range(2, math.floor(math.sqrt(a))+1):
        if a%b == 0:
            flag = False

    return flag

def prime_number(arr):
    length = len(arr)
    ret_arr = [a for a in range(2, length+1) if is_prime(a)]

    return ret_arr

def prime_to_hex(arr):
    ret_arr = [hex(a) for a in arr]

    return ret_arr

def hex_dictionary(arr):
    ret_dict = {}

    for a in arr:
        for char in a[2:]:
            ret_dict[char] = ret_dict[char] + 1 if char in ret_dict.keys() else 1

    return ret_dict

        

def main():
    try:
        n = int(input("Enter array size "))
    except Exception:
        print("Input wasn't a number")
        
    arr = number_generator(n)
    primes = prime_number(arr)
    hexadecimal = prime_to_hex(primes)
    hexdict = hex_dictionary(hexadecimal)
    print("The array is ", arr)
    print("The primes are ", primes)
    print("Primes length is", len(primes))
    print("Hexadecimal values are, ", hexadecimal)
    print("Hexadecimal dictionary is, ", hexdict)

if __name__=="__main__":
    main()


    