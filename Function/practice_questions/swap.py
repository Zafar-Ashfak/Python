# Write a method to swap two numbers.

def swap_with_var(a : int, b: int) -> tuple[int, int]:
    temp = a
    a = b
    b = temp

    return a, b

def swap_without_var(a : int, b : int) -> tuple[int, int]:
    a = a + b
    b = a - b
    a = a- b
    return a, b

def swap_with_xor(a : int, b : int)-> tuple[int, int]:
    a = a ^ b
    b = a ^ b
    a = a ^ b
    return a, b

def main():
    print("Program to swap two numbers.")
    x = int(input("Enter the first number: "))
    y = int(input("Enter the second number: "))

    print("Original numbers")
    print(f"num1 = {x}, num2 = {y}\n")
    # a, b = swap_with_var(x, y)
    # a, b = swap_without_var(x, y)
    a, b = swap_with_xor(x, y)
    print("Swapped numbers")
    print(f"num1 = {a}, num2 = {b}\n")

if __name__ == '__main__':
    main()