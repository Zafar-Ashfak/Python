# Write a Python method to check whether a number is even or odd.

def is_even(num : int) -> bool:
    if num % 2 == 0:
        return True
    else:
        return False

def main():
    num = int(input("Enter a natural number : "))

    res = is_even(num)

    if res:
        print(f"{num} is an even number")
    else:
        print(f"{num} is an odd number")

if __name__ == '__main__':
    main()

