# Write a python method to generate the Fibonacci series up to n terms.

def fibonacci(n: int) -> None:
    first = 0
    second = 1
    i = 0

    while i < n:
        print(first, end=" ")

        next_num = first + second
        first = second
        second = next_num

        i += 1


def main():
    n = int(input("Enter the number of terms: "))
    fibonacci(n)


if __name__ == '__main__':
    main()