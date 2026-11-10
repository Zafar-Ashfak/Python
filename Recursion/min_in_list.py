# Write a Python method to find the minimum element in a list.

def get_min(nums : list[int],i : int = 0, min_element : int = None) -> int:
    if min_element is None:
        min_element = nums[0]

    if i == len(nums):
        return min_element

    if min_element > nums[i]:
        min_element = nums[i]

    return get_min(nums, i + 1, min_element)

def main():
    print("Program to find the maximum element in a list")
    nums = [1, 4, 9, 2, 5, -7, 3, 6]
    res = get_min(nums)
    print(f"Maximum element in the list is: {res}")

if __name__ == '__main__':
    main()

