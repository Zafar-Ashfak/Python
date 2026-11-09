# Write a Python method to remove all occurrences of a particular character. using python

def remove_character(text: str, ch: str) -> str:
    if text == "":
        return ""

    if text[0] == ch:
        return remove_character(text[1:], ch)

    return text[0] + remove_character(text[1:], ch)


def main():
    text = input("Enter a string: ")
    ch = input("Enter a character to remove: ")

    result = remove_character(text, ch)
    print("String after removing character:", result)


if __name__ == "__main__":
    main()