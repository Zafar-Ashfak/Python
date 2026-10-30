def cube(num : int) -> int:
    res = 1
    i = 0
    while i < 3:
        res *= num
        i += 1
    return res


def main():
    num = int(input("Enter a natural number: "))
    res = cube(num)
    print(f"{num} ** 3 = {res}")

if __name__ == '__main__':
    main()