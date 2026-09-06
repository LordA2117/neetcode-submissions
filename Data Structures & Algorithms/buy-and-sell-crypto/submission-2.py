class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = 0  # buy
        max_ = 0

        for sell in range(1, len(prices)):
            profit = prices[sell] - prices[buy]

            if profit < 0:
                buy = sell

            max_ = max(max_, profit)

        return max_
        