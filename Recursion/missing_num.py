def find_sum(arr: list[int], index: int = 0) -> int:
    if index == len(arr):
        return 0

    return arr[index] + find_sum(arr, index + 1)


def main():
    numbers = [1, 2, 3, 4, 6, 7]

    n = len(numbers) + 1

    expected_sum = n * (n + 1) // 2

    actual_sum = find_sum(numbers)

    print(expected_sum - actual_sum)

if __name__ == '__main__':
    main()