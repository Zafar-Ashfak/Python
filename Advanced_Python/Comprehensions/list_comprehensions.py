def multiplication_table(n):

    # *********** Traditional Way ****************

    table = []
    # for i in range(1, 100):
    #     if i % n == 0:
    #         table.append(i)
    #
    # print(table)

    # ************ Smarter Way (List Comprehensions) ************
    table = [i for i in range(1, 100) if i % n == 0]
    print(table)

def main():
    n = int(input("Enter a number: "))
    multiplication_table(n)

main()