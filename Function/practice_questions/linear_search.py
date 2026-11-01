# Write a method to search for an element in an unsorted array.

def linear_search(nums: list[int], target) -> int:
    for e in nums:
        if e == target:
            return nums.index(e)

    return -1


def main():
    print("Program to search for an element in an unsorted array")
    nums = [1, 6, 2, 9, 3, 5, 4, 2, 15, 8, 23]
    target = 5
    res = linear_search(nums, target)
    if res == -1:
        print("Target not found")

    else:
        print(f"Target found at index : {res}")


if __name__ == '__main__':
    main()
