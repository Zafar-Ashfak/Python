# Write a Python method to reverse a list using recursion.

def reverse_list(nums: list[int]) -> list[int]:
    if not nums:
        return []

    return [nums[-1]] + reverse_list(nums[:-1])


def main():
    print("Program to reverse a list using recursion")
    nums = [1, 2, 3, 4, 5]

    res = reverse_list(nums)
    print(f"Reversed list: {res}")


if __name__ == '__main__':
    main()
