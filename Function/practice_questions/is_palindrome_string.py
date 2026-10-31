# Write a method to check whether a string is a palindrome.

def is_palindrome(text : str) -> bool:
    text = text.lower()
    lp = 0
    rp = len(text) - 1

    while lp < rp:
        if text[lp] != text[rp]:
            return False

        lp += 1
        rp -= 1

    return True

def main():
    print("Program to check whether a string is a palindrome")
    text = input("Enter a text: ")
    if is_palindrome(text):
        print(f"{text} is a palindrome string")
    else:
        print(f"{text} is not a palindrome string")

if __name__ == '__main__':
    main()