# Write a Python program to display factorial of a given number

def factorial(num : int) -> int:
    fac = 1

    for i in range(1, num + 1):
        fac *= i

    return fac

def main():
    print("Program to print factorial of a number")
    num = int(input("Enter a natural number: "))
    res = factorial(num)
    print(f"{num}! = {res}")

main()