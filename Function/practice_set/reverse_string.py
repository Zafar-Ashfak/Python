def reverse(text : str) -> str:
    return text[::-1]

def reversestring(text : str) -> str:
    rev = ""
    for ch in text:
        rev = ch + rev

    return rev

def main():
    print("Program to reverse a given string")
    text = input("Enter a string: ")
    res1 = reverse(text)
    res2 = reversestring(text)
    print(res1)
    print(res2)

main()