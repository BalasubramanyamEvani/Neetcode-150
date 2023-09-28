class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        dp = [-1] * n
        curr_min = prices[0]
        for i in range(1, n):
            curr_min = min(prices[i], curr_min)
            dp[i] = curr_min
        max_profit = 0
        for i in range(1, n):
            max_profit = max(max_profit, prices[i] - dp[i])
        return max_profit
        