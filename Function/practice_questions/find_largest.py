# Write a method to find the largest element in an array.

def find_largest(nums : list[int]) -> int:
    largest = nums[0]
    for element in nums:
        if element > largest:
            largest = element

    return largest

def find_largest_opt(nums : list[int]) -> int:
    return max(nums)

def main():
    print("Program to find the largest element in an array")
    nums = [2, 1, 9, 3, 28, 4, 5, 1, 5, 3, 6]
    print(f"Largest number in the list is : {find_largest(nums)}")
    print(f"Largest number in the list is : {find_largest_opt(nums)}")

if __name__ == '__main__':
    main()
