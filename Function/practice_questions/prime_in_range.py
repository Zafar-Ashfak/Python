# Write a method to find all prime numbers in a given range.

from is_prime import is_prime_number

def prime_in_range(n: int, m: int) -> None:
    for i in range(n, m + 1):
        if is_prime_number(i):
            print(i, end=" ")

    return None

def main():
    print("Program to find all prime numbers in a given range")
    n = int(input("Enter the starting range: "))
    m = int(input("Enter the ending range: "))
    prime_in_range(n, m)

if __name__ == '__main__':
    main()
