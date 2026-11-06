# Write a method to find the missing number in an array containing numbers from 1 to n.

def get_missing_number(nums : list[int]) -> int:
    array_sum = 0

    for e in nums:
        array_sum += e

    n = nums[len(nums) - 1]

    contiguous_sum = n * (n + 1) // 2
    # for i in range(1, n + 1):
    #     contiguous_sum += i

    return contiguous_sum - array_sum

def main():
    print("Program to find the missing number in an array containing numbers from 1 to n")
    nums = [1, 2, 3, 5, 6]
    missing_num = get_missing_number(nums)
    print(f"Missing number is: {missing_num}")

if __name__ == '__main__':
    main()