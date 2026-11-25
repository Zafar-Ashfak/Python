# Write a Python method to find the longest word in a given sentence.

def get_longest_word(text: str) -> str:
    words = text.split()

    longest = ""

    for word in words:
        if len(word) > len(longest):
            longest = word
    return longest


def main():
    print("Program to find the longest word in a given sentence")
    text = input("Enter a text: ")
    res = get_longest_word(text)
    print(f"The longest word in the string is: {res}")


if __name__ == '__main__':
    main()

