# Write a Python method to find the maximum element in a list.

def get_max(nums: list[int], i: int = 0, max_element: int = None) -> int:
    if max_element is None:
        max_element = nums[0]

    if i == len(nums):
        return max_element

    if nums[i] > max_element:
        max_element = nums[i]

    return get_max(nums, i + 1, max_element)


def main():
    print("Program to find the maximum element in a list")
    nums = [1, 4, 9, 2, 5, 7, 3, 6]
    res = get_max(nums)
    print(f"Maximum element in the list is: {res}")


if __name__ == '__main__':
    main()
