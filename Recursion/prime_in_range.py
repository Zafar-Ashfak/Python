# Write a Python program to print all prime numbers in a given range.
from is_prime import is_prime

def prime_in_range(n : int, m : int):
    if n > m:
        return

    if is_prime(n):
        print(n, end=" ")

    prime_in_range(n + 1, m)

def main():
    print("Program to print all prime numbers in a given range")
    n = int(input("Enter the starting range: "))
    m = int(input("Enter the ending range: "))
    prime_in_range(n, m)

if __name__ == '__main__':
    main()


