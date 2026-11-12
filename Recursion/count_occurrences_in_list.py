# Write a Python method to count occurrences of an element in a list.

def count_occurrences(nums: list[int], target: int, i: int = 0) -> int:
    if i == len(nums):
        return 0

    if nums[i] == target:
        return 1 + count_occurrences(nums, target, i + 1)

    return count_occurrences(nums, target, i + 1)


def main():
    print("Program to count occurrences of an element in a list")
    nums = [1, 2, 3, 2, 4, 2, 5]
    target = 2

    res = count_occurrences(nums, target)
    print(f"Occurrences of {target} in the list: {res}")


if __name__ == '__main__':
    main()