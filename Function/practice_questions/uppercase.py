uppercase = {
    'a' : 'A',
    'b' : 'B',
    'c' : 'C',
    'd' : 'D',
    'e' : 'E',
    'f' : 'F',
    'g' : 'G',
    'h' : 'H',
    'i' : 'I',
    'j' : 'J',
    'k' : 'K',
    'l' : 'L',
    'm' : 'M',
    'n' : 'N',
    'o' : 'O',
    'p' : 'P',
    'q' : 'Q',
    'r' : 'R',
    's' : 'S',
    't' : 'T',
    'u' : 'U',
    'v' : 'V',
    'w' : 'W',
    'x' : 'X',
    'y' : 'Y',
    'z' : 'Z'
}

def to_uppercase(text : str) -> str:
    new_str = ""
    i = 0
    while i < len(text):
        ch = text[i]
        if ch in uppercase:
            new_str += uppercase[ch]
        else:
            new_str += ch

        i += 1

    return new_str

def main():
    print("Program to convert text into uppercase")
    text = input("Enter a text: ")
    print(to_uppercase(text))

if __name__ == '__main__':
    main()