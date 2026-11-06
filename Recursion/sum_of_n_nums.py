# Write a Python function to calculate sum of n numbers from 1 to n using recursion

def get_sum(n : int) -> int:
    if n == 0:
        return 0

    return n + get_sum(n - 1)

def main():
    print("Program to calculate sum of n numbers from 1 to n using recursion")
    n = int(input("Enter a natural number: "))
    print(f"Sum of numbers from 1 to {n} is: {get_sum(n)}")

if __name__ == '__main__':
    main()
