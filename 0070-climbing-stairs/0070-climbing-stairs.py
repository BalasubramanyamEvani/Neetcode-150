class Solution:
    def climbStairs(self, n: int) -> int:
        dp = [0] * (n + 1)
        dp[0] = 1
        for i in range(1, n + 1):
            one_step = dp[i - 1]
            two_step = dp[i - 2]
            dp[i] = one_step + two_step
        return dp[n]
