# Write a Python method to find the sum of all elements in a list.

def sum_of_elements(nums : list[int], i : int = 0) -> int:
    if i == len(nums):
        return 0

    return nums[i] + sum_of_elements(nums, i + 1)

def main():
    print("Program to find the sum of all elements in a list")
    nums = [1, 2, 3]
    res = sum_of_elements(nums)
    print(f"Sum of elements in the list is: {res}")

if __name__ == '__main__':
    main()