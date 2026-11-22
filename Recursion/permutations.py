# Write a recursive function to generate all possible arrangements (permutations) of characters in a given string.

def permutations(s : str, current : str ="") -> None:
    if len(s) == 0:
        print(current)
        return

    for i in range(len(s)):
        remaining = s[:i] + s[i+1:]

        permutations(remaining, current + s[i])


def main():
    print("Program to generate all possible permutations of characters in a given string")
    s = input("Enter a string \nexample: (ABC)\n")
    permutations(s)

if __name__ == '__main__':
    main()

