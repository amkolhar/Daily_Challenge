"""This problem was asked by Facebook.

Given a array of numbers representing the stock prices of a company in chronological order,
write a function that calculates the maximum profit you could have made from buying and selling that stock once.

You must buy before you can sell it.

For example, given [9, 11, 8, 5, 11, 10], you should return 5, since you could buy the stock at 5 dollars and sell it at 10 dollars."""


def profit(price_range):
    profit = 0
    for i in range(len(price_range)):
        for j in price_range[i+1:]:
            if profit < j - price_range[i]:
                buy = price_range[i]
                sell = j
                profit = sell - buy
            else:
                continue
    print(buy)
    print(sell)
    return profit



price = [2, 11, 8, 5, 7, 10]

print(profit(price))
