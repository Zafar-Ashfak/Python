# Write a Python function to calculate factorial of number using recursion

def factorial(n : int) -> int:
    if n == 1:
        return 1

    return n * factorial(n - 1)

def main():
    print("Program to calculate factorial of number")
    n = int(input("Enter a natural number: "))
    print(f"{n}! = {factorial(n)}")

if __name__ == '__main__':
    main()