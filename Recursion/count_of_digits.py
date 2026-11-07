# Write a Python program to count the digits of a number using recursion

def count_digits(num : int, count : int) -> int:
    # Base Case
    if num == 0:
        return count

    last_digit = num % 10
    count += 1
    return count_digits(num // 10, count)

def main():
    print("Program to count the digits of a number")
    num = int(input("Enter a number: "))
    res = count_digits(num, 0)
    print(f"Total digits of the number {num} is: {res}")

if __name__ == '__main__':
    main()
