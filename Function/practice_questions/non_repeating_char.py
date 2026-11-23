# Write a Python function to find the first character that appears only once in a string.
def print_non_repeating_char(text: str) -> None:
    for char in text:
        count = 0

        for ch in text:
            if char == ch:
                count += 1

        if count == 1:
            print(char)
            break

def main():
    print("Program to find the first character that appears only once in a string")
    text = input("Enter a string: ")
    print_non_repeating_char(text)

if __name__ == '__main__':
    main()
