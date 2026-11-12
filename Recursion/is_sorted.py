# Write a Python method to check whether a list is sorted in ascending order.

def is_sorted(nums : list[int], i : int = 0) -> bool:
    if i == len(nums) - 1:
        return True

    if nums[i] > nums[i + 1]:
        return False

    return is_sorted(nums, i + 1)


def main():
    print("Program to check whether a list is sorted in ascending order")
    nums = [2, 5, 7, 8, 10, 11, 13]
    res = is_sorted(nums)
    if res:
        print("List is sorted")
    else:
        print("List is not sorted")

if __name__ == '__main__':
    main()



