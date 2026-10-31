# Write a method to remove all spaces from a string.

def remove_spaces(text : str) -> str:
    text_list = text.split()
    return "".join(text_list)

def main():
    print("Program to remove all spaces from a string")
    text = input("Enter a text: ")
    print(remove_spaces(text))

if __name__ == '__main__':
    main()