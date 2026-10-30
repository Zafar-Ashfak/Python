# Write a method to calculate the sum of digits of a number.

def sum_of_digits(num : int) -> int:
    res = 0

    while num > 0:
        rem = num % 10
        res += rem
        num //= 10

    return res


def main():
    print("Program to calculate the sum of digits of a number")
    num = int(input("Enter a number: "))
    res = sum_of_digits(num)
    print(f"Sum of digits for number {num} is: {res}")

if __name__ == '__main__':
    main()