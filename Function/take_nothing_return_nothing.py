# Write a Python function that takes no parameters and does not return any value

def add():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    res = num1 + num2

    print(f"{num1} + {num2} = {res}")

def main():
    add()

if __name__== "__main__":
    main()

