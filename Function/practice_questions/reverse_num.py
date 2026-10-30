# Write a Python method to reverse a number.

def method1(num : int) -> None:
    while num > 0:
        rem = num % 10
        print(rem, end="")
        num = num // 10

def reverse(num : int) -> int:
    rev = 0
    while num > 0:
        rem = num % 10
        rev = rev * 10 + rem
        num = num // 10

    return rev

def main():
    num = int(input("Enter a number: "))
    res = reverse(num)
    print(res)

if __name__ == '__main__':
    main()
