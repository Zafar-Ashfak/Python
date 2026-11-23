# Write a Python method to find all pairs of numbers whose sum equals a given target.

def find_pairs(nums: list[int], target: int) -> None:
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] + nums[j] == target:
                print(f"({nums[i]}, {nums[j]})")

def main():
    print("Program to find all pairs of numbers whose sum equals a given target")
    numbers = [2, 7, 4, 5, 3, 8]
    target = 10
    find_pairs(numbers, target)

if __name__ == '__main__':
    main()
