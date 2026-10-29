# Write a Python method to find the maximum of two numbers.

def max_of_two_nums(num1 : int, num2 : int) -> int:
    # if num1 > num2:
    #     return f"{num1} is largest the number in [{num1}, {num2}]"
    # else:
    #     return f"{num2} is largest the number in [{num1}, {num2}]"

    return max(num1, num2)

def main():
    num1 = int(input("Enter the first number : "))
    num2 = int(input("Enter the second number : "))

    res = max_of_two_nums(num1, num2)
    print(f"Largest number in [{num1}, {num2}] is : {res}")

if __name__ == '__main__':
    main()