# Write a Python method to find the second-largest unique number in a list without using sort() or max().

def find_second_largest(nums: list[int]) -> int | float:
    largest = float('-inf')
    second_largest = float('-inf')

    for num in nums:
        if num > largest:
            second_largest = largest
            largest = num

        elif num > second_largest and num != largest:
            second_largest = num

    return second_largest


def main():
    print("Program to find the second-largest unique number in a list.")
    nums = [10, 25, 5, 45, 30, 45]
    res = find_second_largest(nums)
    print(f"The second largest number in the list is: {res}")

if __name__ == '__main__':
    main()
