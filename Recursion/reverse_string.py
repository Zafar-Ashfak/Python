# Write a Python program to reverse a given string using recursion

def reverse_string(text : str) -> str:
    if len(text) == 0:
        return ""

    return reverse_string(text[1:]) + text[0]

def main():
    print("Program to reverse a given string: ")
    text = input("Enter a string")
    res = reverse_string(text)
    print(res)

if __name__ == '__main__':
    main()