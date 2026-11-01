# Write a Python method to calculate the array average.

def calc_average(nums : list[int]) -> float | int:
    res = 0
    for e in nums:
        res += e

    return res / len(nums)

def calc_average_opt(nums : list[int]) -> float | int:
    return sum(nums) / len(nums)

def main():
    print("Program to calculate the array average")
    nums = [1, 2, 3, 4, 5]
    print(f"Average of total numbers in the array is: {calc_average(nums)}")
    print(f"Average of total numbers in the array is: {calc_average_opt(nums)}")

if __name__ == '__main__':
    main()