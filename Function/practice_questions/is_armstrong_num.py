# Write a method to check whether a number is an Armstrong number.
from a_to_the_power import a_to_the_pow
from count_digits import count_digits_opt


def is_armstrong_number(num: int) -> bool:
    org_num = num

    if num < 0:
        raise ValueError("Please enter a non-negative integer")

    power = count_digits_opt(num)
    new_num = 0

    while num > 0:
        rem = num % 10
        new_num += a_to_the_pow(rem, power)
        num //= 10

    return org_num == new_num



def main():
    print("Program to check whether a number is an Armstrong number or not")
    num = int(input("Enter a natural number: "))
    res = is_armstrong_number(num)
    if res:
        print(f"{num} is a armstrong number")
    else:
        print(f"{num} is not a armstrong number")


if __name__ == '__main__':
    main()
