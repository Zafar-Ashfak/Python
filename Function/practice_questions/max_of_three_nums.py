# Write a Python method to find the maximum of three numbers.

def max_of_three_nums(nums : list) -> int:
    return max(nums)

def main():
    print("Program to find the maximum in three numbers")
    nums = []

    i = 0
    while i < 3:
        nums.append(int(input("Enter a number: ")))
        i += 1

    res = max_of_three_nums(nums)
    print(f"{res} is the largest number in {nums}")

if __name__ == '__main__':
    main()