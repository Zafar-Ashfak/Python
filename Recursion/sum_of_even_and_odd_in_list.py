# Write a Python method to find the sum of even and odd elements in a list

def sum_of_even_odd(nums : list[int], i : int = 0, even : int = 0, odd : int = 0) -> tuple[int, int]:
    if i == len(nums):
        return even, odd

    if nums[i] % 2 == 0:
        even += nums[i]

    else:
        odd += nums[i]

    return sum_of_even_odd(nums, i + 1, even, odd)

def main():
    print("Program to find the sum of even and odd elements in a list")
    nums = [1, 4, 7]
    even, odd = sum_of_even_odd(nums)
    print(f"Sum of even numbers in the list is: {even}")
    print(f"Sum of odd numbers in the list is: {odd}")

if __name__ == '__main__':
    main()