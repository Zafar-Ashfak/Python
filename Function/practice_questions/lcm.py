# Write a Python method to find the LCM of two numbers.

def calc_lcm(num1: int, num2: int) -> int:
    i = max(num1, num2)

    while True:
        if i % num1 == 0 and i % num2 == 0:
            return i
        i += 1

def main():
    print("Program to find the LCM of two numbers")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    lcm = calc_lcm(num1, num2)
    print(f"LCM of {num1} and {num2} is: {lcm}")

if __name__ == '__main__':
    main()

