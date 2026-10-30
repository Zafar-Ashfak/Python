# Write a method to print the multiplication table of a number.

def table(num : int):
    if num < 0:
        raise ValueError("Invalid number, please enter natural number")

    for i in range(1, 11):
        print(f"{num} X {i} = {num * i}")

def main():
    print("Program to print the multiplication table of a number")
    num = int(input("Enter a natural number: "))
    table(num)

if __name__ == '__main__':
    main()