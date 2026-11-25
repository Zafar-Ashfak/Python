# Write a Python method to count the number of words in a sentence without using the split() method.

def count_words(text : str) -> int:
    count = 0
    in_word = False

    for char in text:
        if char != " " and not in_word:
            count += 1
            in_word = True

        elif char == " ":
            in_word = False

    return count

def main():
    print("Program to count the number of words in a sentence")
    text = input("Enter a text: ")
    res = count_words(text)
    print(f"The total number of words in the sentence is : {res}")

if __name__ == '__main__':
    main()

