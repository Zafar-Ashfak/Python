# Write a recursive function to check whether a given string is a palindrome.

def is_palindrome(text : str) -> bool:
    if len(text) <= 1:
        return True

    if text[0] != text[-1]:
        return False

    return is_palindrome(text[1:-1])

def main():
    print("Program check whether a given string is a palindrome")
    text = input("Enter a string: ")
    res = is_palindrome(text.lower())
    if res:
        print("String is palindrome")
    else:
        print("String is not palindrome")

if __name__ == '__main__':
    main()

