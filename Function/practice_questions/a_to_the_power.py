# Write a method to calculate the 'a to the power n'.

def a_to_the_pow(base : int, power : int) -> int:
    i = 0
    res = 1

    while i < power:
        res *= base
        i += 1

    return res

def main():
    print("Program to calculate a to the power n")
    base = int(input("Enter the base number: "))
    power = int(input("Enter the power number: "))

    res = a_to_the_pow(base, power)

    print(f"{base} ^ {power} = {res}")

if __name__ == '__main__':
    main()

