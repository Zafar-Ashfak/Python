# Write a function that takes parameters but doesn't return any value.

# Function definition
def division(num1 : int, num2 : int):
    res = num1 / num2
    print(f"{num1} / {num2} = {res}")

def main(): # main function definition
    num1 = int(input("Enter the first number: "))
    num2 = int(input("Enter the second number: "))
    division(num1, num2) # function call

main() # main function call