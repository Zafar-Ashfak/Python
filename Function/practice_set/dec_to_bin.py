# Write a program to convert a decimal number into binary number using recursion

# using str() method
def dec_to_bin(dec : int) -> str:

    # Base Case
    if dec == 0:
        return ""

    # Recursive Call
    rem = dec % 2
    return dec_to_bin(dec // 2) + str(rem)

# using numerals
def dec_to_bin_opt(dec : int) -> int:
    # Base Case
    if dec == 0:
        return 0

    # Recursive Call
    rem = dec % 2
    return rem + 10 * dec_to_bin_opt(dec // 2)

def main():
    print("Program to convert a decimal number to binary")
    dec = int(input("Enter a decimal number: "))
    # bin_num = dec_to_bin(dec)
    bin_num = dec_to_bin_opt(dec)
    print(f"({dec})10 = ({bin_num})2")

main()