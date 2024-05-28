class Solution:
    def minSteps(self, n: int) -> int:
        dp = [math.inf] * (n + 1)
        dp[1] = 0
        for i in range(2, n + 1):
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + 1 + ((i - j) // j))
                    other = i // j
                    dp[i] = min(dp[i], dp[other] + 1 + ((i - other) // other))
        return dp[-1]
