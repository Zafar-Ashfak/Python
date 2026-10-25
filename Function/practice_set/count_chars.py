def count_chars(text : str) -> int:
    return len(text)

def main():
    print("Program to count characters of the given string")
    text = input("Enter a text: ")
    print(f"The total characters in the text is: {count_chars(text)}")

main()