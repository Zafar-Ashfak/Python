# Write a program to print numbers from N to 1 using recursion.

def n_to_1(n : int):
    # Base Case
    if n == 0:
        return

    print(n, end=" ")
    n_to_1(n - 1)

def main():
    print("Program to print numbers from N to 1")
    n = int(input("Enter a natural number: "))
    n_to_1(n)

if __name__ == '__main__':
    main()