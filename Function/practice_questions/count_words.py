# Write a Python method to count the number of words in a string.

def count_words(text : str) -> int:
    return len(text.split())

def main():
    print("Program to count the number of words in a string")
    text = input("Enter a text: ")
    print(f"Total words in the string is: {count_words(text)}")

if __name__ == '__main__':
    main()