# Write a Python function that takes parameters but does not return any value

def sub(num1, num2):
    res = num1 - num2
    print(f"{num1} - {num2} = {res}")

def main():
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    sub(num1, num2)

if __name__ == '__main__':
    main()
