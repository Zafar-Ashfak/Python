# Write a Python program to check if a given number is prime or not

def isprime(num : int) -> bool:
    if num < 2:
        return False

    for i in range(2, num):
        if num % i == 0:
            return False

    return True


def main():
    print("Program to check if a number is prime")
    num = int(input("Enter a natural number: "))
    res = isprime(num)
    if res:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

main()