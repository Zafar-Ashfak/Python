# Write a Python method to calculate the square of a number.

def square(num : int) -> int:
    return num ** 2

def square_with_logic(num : int) -> int:
    i = 0
    res = 1
    while i < 2:
        res = res * num
        i += 1

    return  res


def main():
    num = int(input("Enter a natural number : "))
    # res = square(num)
    res = square_with_logic(num)
    print(f"{num} ** 2 = {res}")

if __name__ == '__main__':
    main()
