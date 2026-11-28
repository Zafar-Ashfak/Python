# Write a Python program to calculate and print the sum of every row.


def sum_of_row(matrix : list[list[int]]):
    for row in matrix:
        total = 0

        for num in row:
            total += num

        print(total)

def main():
    matrix = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    sum_of_row(matrix)

if __name__ == '__main__':
    main()
