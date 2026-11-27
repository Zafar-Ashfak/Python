# Given two strings s and t, find the smallest substring of s containing all characters of t, including their required frequencies.

from collections import Counter

def min_window_substr(s: str, t: str) -> None:
    required = Counter(t)
    window = {}

    left = 0
    formed = 0
    required_count = len(required)

    min_length = float("inf")
    start = 0

    for right in range(len(s)):

        char = s[right]
        window[char] = window.get(char, 0) + 1

        if char in required and window[char] == required[char]:
            formed += 1

        while formed == required_count:

            if right - left + 1 < min_length:
                min_length = right - left + 1
                start = left

            left_char = s[left]
            window[left_char] -= 1

            if left_char in required and window[left_char] < required[left_char]:
                formed -= 1

            left += 1

    if min_length == float("inf"):
        print("")
    else:
        print(s[start:start + min_length])

def main():
    s = "ADOBECODEBANC"
    t = "ABC"

    min_window_substr(s, t)

if __name__ == '__main__':
    main()


