# Write a method to check whether two strings are equal without using equals().

def are_equal(text1: str, text2: str) -> bool:
    text1 = text1.lower()
    text2 = text2.lower()

    if len(text1) != len(text2):
        return False

    i = 0
    while i < len(text1):
        if text1[i] != text2[i]:
            return False
        i += 1

    return True


def main():
    print("Program to check whether two strings are equal")
    text1 = input("Enter the first text: ")
    text2 = input("Enter the second text: ")

    if are_equal(text1, text2):
        print("Both string are equal ✅")
    else:
        print("String are not equal ❌")


if __name__ == '__main__':
    main()
