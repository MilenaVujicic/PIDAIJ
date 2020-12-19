import sequential as s
import sys


def main():
    choice = "none"
    while choice != "5":
        print("1. Sequential")
        print("2. List comprehension")
        print("3. Generator")
        print("4. Multiprocessing")
        print("5. Exit")
        choice = input("Enter the choice number ")

        if choice == "1":
            (n, m) = s.size_input()
            if n is None or m is None:
                sys.exit(1)
            spec = s.special_input(n, m)
            print(spec)
            matrix = s.generate_cords(n, m, spec)
            print(matrix)
            s.calculate_special_field_distance(matrix, spec)
        elif choice == "2":
            ...
        elif choice == "3":
            ...
        elif choice == "4":
            ...
        elif choice == "5":
            sys.exit(0)


if __name__ == "__main__":
    main()
