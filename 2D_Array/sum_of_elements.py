# Write a python method to calculate the sum of all elements in a 2D array.


def sum_of_elements(matrix : list[list[int]]) -> int:
    total = 0

    for row in matrix:
        for num in row:
            total += num

    return total

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    res = sum_of_elements(matrix)
    print(f"The sum of all elements of the matrix is: {res} ")

if __name__ == '__main__':
    main()