# Write a Python function to find the sum of even and odd digits of a number.

def sum_of_even_and_odd(num : int, even : int = 0, odd : int = 0) -> tuple[int, int]:
    num = abs(num)

    if num == 0:
        return even, odd

    rem = num % 10

    if rem % 2 == 0:
        even += rem
    else:
        odd += rem

    return sum_of_even_and_odd(num // 10, even, odd)

def main():
    print("Program to find the sum of even and odd digits of a number")
    num = int(input("Enter a number: "))
    even, odd = sum_of_even_and_odd(num)
    print(f"Sum of even numbers in the number {num} is: {even}")
    print(f"Sum of odd numbers in the number {num} is: {odd}")

if __name__ == '__main__':
    main()
