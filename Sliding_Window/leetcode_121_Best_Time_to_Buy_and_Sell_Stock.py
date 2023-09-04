"""
You are given an array prices where prices[i]
is the price of a given stock on the ith day.

You want to maximize your profit by choosing a
single day to buy one stock and choosing a different day in the
future to sell that stock.

Return the maximum profit you can achieve from this transaction.
If you cannot achieve any profit, return 0.
"""


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        min_prices = [prices[0]]
        for price in prices[1:]:
            current_profit = price - min_prices[-1]
            if current_profit > max_profit:
                max_profit = current_profit
            elif price < min_prices[-1]:
                min_prices.append(price)
        return max_profit
