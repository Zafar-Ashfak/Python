# Given a list of words, group words that are anagrams of each other.

def group_anagram(words : list[str]) -> list[str]:
    groups = {}

    for word in words:

        key = "".join(sorted(word))

        if key not in groups:
            groups[key] = []

        groups[key].append(word)

    return list(groups.values())

def main():
    words = ["eat", "tea", "tan", "ate", "nat", "bat"]
    res = group_anagram(words)
    print(res)

if __name__ == '__main__':
    main()
