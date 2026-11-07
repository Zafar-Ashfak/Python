# Write a Python program to find the product of digits of a number.

def product_of_digits(num : int, prod : int = 1) -> int:
    # Base Case
    if num == 0:
        return prod

    last_digit = num % 10
    prod *= last_digit
    return product_of_digits(num // 10, prod)

def main():
    print("Program to calculate the product of digits of a number")
    num = int(input("Enter a number: "))
    res = product_of_digits(num)
    print(f"Product of digits of the number {num} is : {res}")

if __name__ == '__main__':
    main()