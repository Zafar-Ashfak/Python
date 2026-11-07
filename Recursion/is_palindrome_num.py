# Write a Python program to check whether a number is a palindrome.

def is_palindrome(num : int, rev : int = 0) -> int:

    if num == 0:
        return rev

    rem = num % 10
    rev = rev * 10 + rem

    return is_palindrome(num // 10, rev)

def main():
    print("Program to check is whether a number is a palindrome")
    num = int(input("Enter a number: "))
    res = is_palindrome(num)
    if num == res:
        print(f"{num} is a palindrome number")
    else:
        print(f"{num} is not a palindrome number")

if __name__ == '__main__':
    main()