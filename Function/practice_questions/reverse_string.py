# Write a Python method to reverse a string.

def reverse_brute(text : str) -> str:
    rev_str = ""
    for ch in text:
        rev_str = ch + rev_str

    return rev_str

def reverse(text : str) -> str:
    return text[::-1]

def main():
    print("Program to reverse a string")
    text = input("Enter a text: ")
    print(reverse(text))
    print(reverse_brute(text))

if __name__ == '__main__':
    main()




