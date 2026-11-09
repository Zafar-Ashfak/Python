# Write a Python function to find the length of a string without using len()

def string_length(text: str) -> int:
    if text == "":
        return 0

    return 1 + string_length(text[1:])


def main():
    text = input("Enter a string: ")
    print(f"Length of the string is: {string_length(text)}")


if __name__ == "__main__":
    main()