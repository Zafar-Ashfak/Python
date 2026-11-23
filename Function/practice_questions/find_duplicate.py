# Write a Python program to find all duplicate elements without using set() or Counter.

def find_duplicate(nums : list[int]) -> None:
    duplicates = []

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[i] == nums[j] and nums[i] not in duplicates:
                duplicates.append(nums[i])

    print(duplicates)

def main():
    numbers = [1, 2, 3, 2, 4, 5, 1, 6]
    print("Program to find all duplicate elements in a list")
    find_duplicate(numbers)

if __name__ == '__main__':
    main()
