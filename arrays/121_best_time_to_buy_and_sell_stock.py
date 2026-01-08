#Easy
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        profit = 0
        max_profit = 0
        buy = prices[0]
        for sell in prices[1:]:
            profit = sell - buy
            if sell < buy:
                buy = sell
            max_profit = max(profit, max_profit)

        return max_profit

# Time Complexity : O(n)
# Space Complexity : O(n)