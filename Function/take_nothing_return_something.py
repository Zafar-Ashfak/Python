# Write a Python function that takes no parameters but return a value

def product():
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    return num1 * num2

def main():
    print("Program to calculate the product of decimal numbers")
    res = product()
    print(f"The product is: {res}")

if __name__ == '__main__':
    main()
