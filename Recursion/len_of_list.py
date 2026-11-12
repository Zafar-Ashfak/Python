# Write a Python program to count length of the list

def get_length(nums: list[int]) -> int:
    if not nums:
        return 0

    return 1 + get_length(nums[1:])


def main():
    print("Program to find the length of a list")
    nums = [10, 20, 30, 40, 50]
    res = get_length(nums)
    print(f"Length of the list is: {res}")


if __name__ == '__main__':
    main()
