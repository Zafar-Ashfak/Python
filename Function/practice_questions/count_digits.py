# Write a Python method to count the digits in a number.

def count_digits(num : int) -> int:
    count = 0

    num = abs(num)

    if num == 0:
        return 1

    while num > 0:
        count += 1
        num //= 10

    return count

def count_digits_opt(num : int) -> int:
    num = str(abs(num))
    return len(num)

def main():
    num = int(input("Enter a number: "))
    print(f"The total number of digits in the number {num} is: {count_digits(num)}")
    print(f"The total number of digits in the number {num} is: {count_digits_opt(num)}")

if __name__ == '__main__':
    main()
