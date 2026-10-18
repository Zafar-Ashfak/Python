# Write a function to calculate the sum of first n natural number

def sum_of_n_nums(n : int) -> int:
    s = 0
    for i in range(1, n + 1):
        s += i

    return s

def main():
    print("Program to print sum of n natural number")
    n = int(input("Enter a natural number: "))
    res = sum_of_n_nums(n)
    print(f"Sum of {n} natural number is: {res}")

main()