# Write a Python method to count the occurrences of a character in a string.

def count_occurrences(text: str, ch: str) -> int:
    if text == "":
        return 0

    if text[0] == ch:
        return 1 + count_occurrences(text[1:], ch)

    return count_occurrences(text[1:], ch)


def main():
    text = input("Enter a string: ")
    ch = input("Enter a character: ")

    result = count_occurrences(text, ch)
    print(f"Occurrences of '{ch}' in '{text}': {result}")


if __name__ == "__main__":
    main()