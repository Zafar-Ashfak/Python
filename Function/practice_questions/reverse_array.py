# Write a method to reverse an array

def reverse_arr(nums : list[int]):
    # i = len(nums) - 1
    # while i >= 0:
    #     print(nums[i], end=' ')
    #     i -= 1
    #
    #

    for i in range((len(nums) -1), -1, -1):
        print(nums[i], end= ' ')


def main():
    print("Program to find the LCM of two numbers")
    nums = [1, 4, 2, 7, 9, 4, 6]
    reverse_arr(nums)

if __name__ == '__main__':
    main()