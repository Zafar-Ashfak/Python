# Write a Python program to check whether a number is prime or not

def is_prime_number(num : int) -> bool:
    is_prime = True

    if num < 2:
        is_prime = True

    for i in range(2, num):
        if num % 2 == 0:
            is_prime = False

    return is_prime

def main():
    num = int(input("Enter a natural number: "))
    res = is_prime_number(num)

    if res:
        print(f"{num} is a prime number")
    else:
        print(f"{num} is not a prime number")

if __name__ == '__main__':
    main()