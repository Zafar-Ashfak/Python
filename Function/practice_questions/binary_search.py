# Write a method to search for an element in a sorted array.

def binary_search(nums : list[int], target) -> int:
    si = 0
    ei = len(nums) - 1

    while si <= ei:
        mid =  int(si + (ei - si) / 2)
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            si = mid + 1
        else:
            ei = mid - 1

    return -1

def main():
    print("Program to search for an element in a sorted array")
    nums = [2, 3, 6, 9, 10, 17, 19, 23, 29, 30]
    target = 23

    res = binary_search(nums, target)
    if res == -1:
        print("Target not found")
    else:
        print(f"Target found at index: {res}")

if __name__ == '__main__':
    main()