# Write a Python method to check whether a number is a palindrome.
from reverse_num import reverse

def palindrome(num : int):
    rev = reverse(num)

    if rev == num:
        print(f"{num} is a palindrome number")
    else:
        print(f"{num} is not a palindrome number")

def main():
    num = int(input("Enter a number: "))
    palindrome(num)

if __name__ == '__main__':
    main()