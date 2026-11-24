# Write a recursive function to find the second-largest unique number without using sort() or max().

def second_largest(
        arr : list[int],
        index : int = 0,
        largest : float | int =float('-inf'),
        second : float | int = float('-inf')
):

    if index == len(arr):
        return second

    num = arr[index]

    if num > largest:
        second = largest
        largest = num

    elif second < num < largest:
        second = num

    return second_largest(arr, index + 1, largest, second)


def main():
    numbers = [8, 25, 5, 15, 30, 20]

    print(f"The second largest number in the list is: {second_largest(numbers)}")

if __name__ == '__main__':
    main()