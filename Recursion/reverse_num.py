# Write a Python method to reverse a number using recursion.

def reverse(num: int, rev: int = 0) -> int:
    if num == 0:
        return rev

    rem = num % 10
    rev = rev * 10 + rem

    return reverse(num // 10, rev)

def main():
    print("Program to reverse a number")
    num = int(input("Enter a number: "))
    print(reverse(num))

if __name__ == '__main__':
    main()