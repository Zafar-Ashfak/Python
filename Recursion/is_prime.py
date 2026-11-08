# Write a Python program to check whether a number is prime.

def is_prime(num: int, i: int = 2) -> bool:

    if num < 2:
        return False

    if i * i > num:
        return True

    if num % i == 0:
        return False

    return is_prime(num, i + 1)
def main():
    print("Program to check whether a number is prime")
    num = int(input("Enter a natural number: "))
    if is_prime(num):
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

if __name__ == '__main__':
    main()