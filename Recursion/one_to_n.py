# Write a python function to print numbers from 1 to n using recursion.

def one_to_n(n : int):
    # Base Case
    if n == 0:
        return

    one_to_n(n - 1)
    print(n, end=" ")

def main():
    print("Program to print numbers from 1 to n")
    n = int(input("Enter a natural number: "))
    one_to_n(n)

if __name__ == '__main__':
    main()

