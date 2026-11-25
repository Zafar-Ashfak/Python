# Check whether two strings contain the same characters with the same frequencies, regardless of order.

def is_anagram(s1 : str, s2 : str) -> bool:
    if sorted(s1) == sorted(s2):
        return True
    else:
        return False

def main():
    print("Program to check whether two strings are anagram")
    s1 = input("Enter the first string: ")
    s2 = input("Enter the second string: ")

    if is_anagram(s1, s2):
        print(f"'{s1}' and '{s2}' are anagram")
    else:
        print(f"'{s1}' and '{s2}' are not anagram")

if __name__ == '__main__':
    main()
