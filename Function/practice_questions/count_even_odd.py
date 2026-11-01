# Write a method to count even and odd elements in a number and in an array.

def count_even_odd(num: int) -> tuple[int, int]:
    even = 0
    odd = 0

    while num > 0:
        rem = num % 10
        if rem % 2 == 0:
            even += 1
        else:
            odd += 1

        num //= 10

    return even, odd

def count_even_odd_arr(nums : list[int]) -> tuple[int, int]:
    even = 0
    odd = 0
    for e in nums:
        if e % 2 == 0:
            even += 1
        else:
            odd +=1
    return even, odd


def main():
    # print("to count even and odd elements in a number")
    # num = int(input("Enter a number: "))
    # even, odd = count_even_odd(num)
    # print(f"The total number of evens in the number is: {even}")
    # print(f"The total number of odds in the number is: {odd}")

    print("to count even and odd elements in an array")
    arr = [1, 5, 2, 6, 2, 6, 9, 4, 3, 5, 7]
    even, odd = count_even_odd_arr(arr)
    print(f"The total number of evens in the number is: {even}")
    print(f"The total number of odds in the number is: {odd}")


if __name__ == '__main__':
    main()
