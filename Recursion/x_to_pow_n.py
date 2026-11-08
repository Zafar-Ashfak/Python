# Write a Python program to calculate the power of a number (xⁿ).

def power(x : int, n : int) -> int:
   if n == 0:
       return 1

   return x * power(x, n - 1)

def main():
    print("Program to calculate the power of a number (xⁿ)")
    x = int(input("Enter the base number: "))
    n = int(input("Enter the power: "))
    res = power(x, n)
    print(f"{x}^{n} = {res}")

if __name__ == '__main__':
    main()