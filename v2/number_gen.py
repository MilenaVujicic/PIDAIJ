def number_generator(n):
    arr = []
    for i in range(1, n+1):
        arr.append(i)
    
    return arr

try:
    n = int(input("Enter array size"))
except Exception:
    print("Input wasn't a number")
    
arr = number_generator(n)
print(arr)