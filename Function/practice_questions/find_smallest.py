# Write a method to find the smallest element in an array.

def find_smallest(nums : list[int]) -> int:
    smallest = nums[0]

    for element in nums:
        if element < smallest:
            smallest = element

    return smallest

def find_smallest_opt(nums : list[int]) -> int:
    return min(nums)

def main():
    print("Program to find the smallest element in an array")
    nums = [12, 9, 3, 28, 4, 5, 5, 3, 6]
    print(f"Smallest number in the list is : {find_smallest(nums)}")
    print(f"Smallest number in the list is : {find_smallest_opt(nums)}")

if __name__ == '__main__':
    main()