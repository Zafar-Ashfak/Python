# Write a Python program to check if a given number is palindrome or not

def is_palindrome(num : int) -> int:
    rev = 0

    while num > 0:
        rem = num % 10
        rev = (rev * 10) + rem
        num //= 10

    return rev

def main():
    print("Program to check if a given number is palindrome")
    num = int(input("Enter a number: "))
    org = num
    res = is_palindrome(num)
    if org == res:
        print(f"{org} is a palindrome number")
    else:
        print(f"{org} is not a palindrome number")

main()
