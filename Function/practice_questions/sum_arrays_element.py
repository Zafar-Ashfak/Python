# Write a Python method to calculate the sum of array elements.

def sum_of_array_elements(nums : list[int]) -> int:
    res = 0
    for e in nums:
        res += e

    return res

def sum_of_array_elements_opt(nums : list[int]) -> int:
    return sum(nums)


def main():
    print("Program to calculate the sum of array elements")
    nums = [2, 1, 9, 4, 7, 0, 3, 6]
    print(f"Sum of all elements in the array is: {sum_of_array_elements(nums)}")
    print(f"Sum of all elements in the array is: {sum_of_array_elements_opt(nums)}")

if __name__ == '__main__':
    main()