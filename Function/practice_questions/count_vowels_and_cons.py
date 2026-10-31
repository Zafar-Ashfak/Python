# Write a Python method to count vowels and consonants in a string

def count(text : str) -> tuple[int, int]:
    vowel_letters = "aeiou"

    vowels = 0
    consonants = 0
    for ch in text.lower():
        if ch in vowel_letters:
            vowels += 1
        elif ch.isalpha():
            consonants += 1

    return vowels, consonants


def main():
    print("Program to count vowels and consonants")
    text = input("Enter a text: ")
    vowels, consonants  = count(text)

    print(f"Total vowels: {vowels}")
    print(f"Total consonants: {consonants}")

if __name__ == '__main__':
    main()




