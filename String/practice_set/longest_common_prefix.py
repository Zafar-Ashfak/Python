# Given a list of strings, find the longest common prefix shared by all strings.

def get_longest_common_prefix(words: list[str]) -> str:
    prefix = words[0]

    for word in words[1:]:

        while not word.startswith(prefix):
            prefix = prefix[:-1]

            if not prefix:
                break

    return prefix

def main():
    words = ["flower", "flow", "flight"]
    res = get_longest_common_prefix(words)
    print(f"The longest common prefix is: {res}")

if __name__ == '__main__':
    main()
