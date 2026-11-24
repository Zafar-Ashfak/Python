# Write a recursive function to find all pairs whose sum equals the target value.

def find_pairs(arr : list[int], target, i : int = 0, j: int = 1):

    if i >= len(arr) - 1:
        return None

    if j >= len(arr):
        return find_pairs(arr, target, i + 1, i + 2)

    if arr[i] + arr[j] == target:
        print(f"({arr[i]}, {arr[j]})")

    return find_pairs(arr, target, i, j + 1)

def main():

    numbers = [2, 7, 4, 5, 3, 8]
    find_pairs(numbers, 10)

if __name__ == '__main__':
    main()