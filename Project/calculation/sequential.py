import math


def size_input():
    try:
        n = int(input("Enter matrix width "))
        m = int(input("Enter matrix height "))
    except Exception:
        print("Input wasn't a whole number")
        return None, None

    return n, m


def special_input(n, m):
    arr = []

    try:
        l = int(input("Enter the number of special fields "))
    except Exception:
        print("Input wasn't a whole number")
        return None, None

    for i in range(0, l):
        try:
            x = int(input("Enter x position "))
            y = int(input("Enter y position "))

            if x > n or y > m:
                print("Coordinates are not valid")
                return None

            arr.append((x, y))
        except Exception:
            print("Input wasn't a whole number")
            return None

    return arr


def generate_cords(n, m, spec):
    cords = []

    for i in range(0, n):
        for j in range(0, m):
            for k in range(0, len(spec)):
                x, y = spec[k]
                if x == i and y == j:
                    cords.append((i, j, 'x'))
                else:
                    cords.append((i, j, 0))

    return cords


def calculate_cord_distance(cord1, cord2):
    x1, y1 = cord1
    x2, y2 = cord2

    distance = math.sqrt((x2-x1)**2+(y2-y1)**2)

    return distance


def calculate_special_field_distance(cords, spec):

    distances = []
    for i in range(0, len(cords)):
        x, y, t = cords[i]
        for k in range(0, len(spec)):
            xs, ys = spec[k]
            if t != 'x':
                c1 = (x,y)
                c2 = (xs, ys)
                d = calculate_cord_distance(c1, c2)
                distances.append((d, k))

    print(distances)

