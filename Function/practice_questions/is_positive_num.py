# Write a method to check whether a number is positive, negative, or zero.

def is_positive(num : int) -> str:
    if num == 0:
        return "Zero"
    elif num > 0:
        return "Positive"
    else:
        return "Negative"

def main():
    num = int(input("Enter an integer number : "))
    res = is_positive(num)
    print(res)

if __name__ == '__main__':
    main()