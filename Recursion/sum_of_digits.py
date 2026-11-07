# write a program to find the sum of digits of a number using recursion.

def sum_of_digits(num : int, total_sum : int) -> int:
    if num == 0:
        return total_sum

    rem = num % 10
    total_sum += rem
    return sum_of_digits(num // 10, total_sum)

def main():
    print("Program to find the sum of digits of a number")
    num = int(input("Enter a number: "))
    res = sum_of_digits(num, 0)
    print(f"Sum of digits in number {num} is: {res}")

if __name__ == '__main__':
    main()



