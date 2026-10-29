# Write a Python function that takes some parameters and return some value

def greet(name : str, age : int) -> str:
    if age < 18:
        return f"Sorry Mr / Mrs, {name}.\nYou are not eligible to vote"
    else:
        return f"Hello! Mr / Mrs, {name}.\nYou are eligible to vote"

def main():
    print("Program to check to vote eligibility")
    name = input("Enter your name: ")
    age = int(input("Enter your age: "))

    res = greet(name, age)
    print(res)

if __name__ == '__main__':
    main()