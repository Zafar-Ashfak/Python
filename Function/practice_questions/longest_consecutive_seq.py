# Write a Python program to find the length of the longest sequence of consecutive numbers in an unsorted list.

def longest_consecutive_sequence(nums: list[int]) -> int:
    longest = 0

    for num in nums:

        if num - 1 not in nums:
            current = num
            count = 1

            while current + 1 in nums:
                current += 1
                count += 1

            if count > longest:
                longest = count

    return longest

def main():
    nums = [100, 4, 200, 1, 3, 2]
    res = longest_consecutive_sequence(nums)
    print(f"The longest consecutive sequence in the list is: {res}")

if __name__ == '__main__':
    main()
