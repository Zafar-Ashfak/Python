# Write a python function to check leap years

def is_leap_year(year : int) -> bool:
    a = year % 4 == 0
    b = year % 100 != 0
    c = year % 100 == 0 and year % 400 == 0

    if (a and b) or c:
        return True

    return False

def main():
    print("Program to check leap years")
    year = int(input("Enter a year: "))
    if is_leap_year(year):
        print(f"{year} is a leap year")
    else:
        print(f"{year} is not a leap year")

if __name__ == '__main__':
    main()
