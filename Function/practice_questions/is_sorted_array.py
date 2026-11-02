# Write a method to check whether an array is sorted.

def is_sorted_array(nums : list[int]) -> bool:
    i = 0
    while i < len(nums) - 1:
        if nums[i] > nums[i + 1]:
            return False

        i += 1

    return True

def main():
    print("Program to check whether an array is sorted")
    nums = [2, 3, 7, 8, 15, 21, 28, 30]
    res = is_sorted_array(nums)
    if res:
        print("Yes, Array is sorted")
    else:
        print("No, Array is not sorted")

if __name__ == '__main__':
    main()