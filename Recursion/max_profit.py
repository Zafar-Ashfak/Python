# Write a Python method to find the maximum profit by buying once and selling once later.

def max_profit(prices : list[int], index : int=0, min_price : float | int = float('inf'), profit : int=0):
    if index == len(prices):
        return profit

    price = prices[index]

    if price < min_price:
        min_price = price

    current_profit = price - min_price

    if current_profit > profit:
        profit = current_profit

    return max_profit(prices, index + 1, min_price, profit)


def main():
    prices = [7, 1, 5, 3, 6, 4]
    print(f"Maximum profit in the prices list: {max_profit(prices)}")

if __name__ == '__main__':
    main()