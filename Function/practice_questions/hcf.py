# Write a Python method to find the GCD (HCF) of two numbers.

def hcf(num1 : int, num2 : int) -> int:
    min_num = min(num1, num2)

    i = 2
    gcd = 1
    while i <= min_num / 2:
        if num1 % i == 0 and num2 % i == 0:
            gcd = i
        i += 1
    return gcd

def main():
    print("Program to find the GCD (HCF) of two numbers")
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    gcd = hcf(num1, num2)
    print(f"Greatest Common Divisor of [{num1}, {num2}] is : {gcd}")

if __name__ == '__main__':
    main()


