## 121. Best Time to Buy and Sell Stock
# Two Pointer, L is buy pointer(i) and R is sell pointer(k) if R - L is negative, then iterate R plus one and make L = R - 1, if R - L is positive, iterate only R and keep track of R - L value using max() built-in python function
class Solution:
    def maxProfit(self, prices: list) -> int:
        max_sum = 0
        i = 0
        k = 1
        while i < k and k < len(prices):
            if prices[k] - prices[i] < 0:
                k += 1
                i = k - 1
            elif prices[k] - prices[i] >= 0:
                max_sum = max(max_sum, prices[k] - prices[i])
                k += 1
        return max_sum
    
"""
You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

Example 2:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: In this case, no transactions are done and the max profit = 0.
"""
