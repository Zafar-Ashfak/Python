# Write a method to count the occurrences of a character in a string.

def count_occurrences(text : str, ch : str) -> int:
    count = 0
    for e in text.lower():
        if e == ch.lower():
            count += 1

    return count

def count_occurrence_with_function(text : str, ch : str) -> int:
    return text.lower().count(ch.lower())

def main():
    print("Program to count the occurrences of a character in a string")
    text = input("Enter a text: ")
    ch = input("Enter the character you want to check in the text: ")
    print(f"{ch} occurs {count_occurrences(text, ch)} times in the text")
    print(f"{ch} occurs {count_occurrence_with_function(text, ch)} times in the text")

if __name__ == '__main__':
    main()
