# Write a Python method to search for an element in a list.

def search(nums : list[int], key : int, i : int = 0) -> int:
    if i == len(nums):
        return -1

    if nums[i] == key:
        return i

    return search(nums, key, i + 1)


def main():
    print("Program to search for an element in a list")
    nums = [1, 6, 2, 3, 9, 5, 7, 8, 4, 15, 11, 18, 14, 16, 12, 17, 13]
    key = 3
    res = search(nums, key)
    if res == -1:
        print("Key not found")
    else:
        print(f"Key found at index : {res}")

if __name__ == '__main__':
    main()




