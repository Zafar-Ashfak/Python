# Write a Python method to rotate a list to the right by K positions without using slicing.

def rotate(nums : list[int], k : int) -> list[int]:

    n = len(nums)
    k = k % n

    for _ in range(k):
        last = nums[-1]

        for i in range(n - 1, 0, -1):
            nums[i] = nums[i - 1]

        nums[0] = last

    return nums

def main():
    print("Program to rotate a list to the right by K positions")
    nums = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    k = int(input("Enter the value for k: "))
    res = rotate(nums, k)
    print(res)

if __name__ == '__main__':
    main()