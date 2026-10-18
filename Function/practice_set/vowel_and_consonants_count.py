# Write a Python program to count and display vowels and consonants in a given string

def count(text : str):
    text = text.lower()

    vowels = 0
    consonants = 0

    for ch in text:
        if ch in 'aeiou':
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    print(f"The number of vowels in the string is: {vowels}")
    print(f"The number of consonants in the string is: {consonants}")

def main():
    print("Program to count vowels and consonants in a string")
    text = input("Enter a string: ")
    count(text)

main()

