# Write a Python method to find the character that appears most frequently in a string.

def most_frequent_char(text: str) -> tuple[str, int]:
    max_count = 0
    result = ""

    for char in text.replace(" ", ""):
        count = text.count(char)

        if count > max_count:
            max_count = count
            result = char

    return result, max_count

def main():
    print("Program to find the character that appears most frequently in a string")
    text = input("Enter a string: ")
    result, max_count = most_frequent_char(text)
    print(f"Character '{result}' appears {max_count} times in the string")

if __name__ == '__main__':
    main()

