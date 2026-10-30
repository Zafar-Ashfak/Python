# Write a Python method to calculate the factorial of a number.

def factorial(num : int) -> int:
    fac = 1
    for i in range(1, num + 1):
        fac *= i

    return fac

def main():
    num = int(input("Enter a natural number: "))
    res = factorial(num)
    print(f"{num}! = {res}")

if __name__ == '__main__':
    main()