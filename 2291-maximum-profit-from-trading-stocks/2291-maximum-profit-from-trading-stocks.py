class Solution:
    def maximumProfit(self, present: List[int], future: List[int], budget: int) -> int:
        N = len(present)
        weights = [num for num in present]
        vals = [future[i] - present[i] for i in range(N)]
        vals = [val if val > 0 else 0 for val in vals]
        dp = [[0] * (budget + 1) for _ in range(N + 1)]
        
        for i in range(1, N + 1):
            for j in range(budget + 1):
                dp[i][j] = max(
                    dp[i - 1][j],
                    (vals[i - 1] + dp[i - 1][j - weights[i - 1]]) if weights[i - 1] <= j and vals[i - 1] > 0 else dp[i - 1][j]
                )
        return dp[-1][-1]

        # N = len(present)
        # cache = {}
        # def dfs(i, currsum):
        #     if i == N:
        #         return 0
        #     if (i, currsum) in cache:
        #         return cache[(i, currsum)]
        #     if currsum > budget:
        #         return 0
        #     exclude = dfs(i + 1, currsum)
        #     val = future[i] - present[i]
        #     weight = present[i]
        #     include = -1
        #     if currsum + weight <= budget and val > 0:
        #         include = val + dfs(i + 1, currsum + weight)
        #     cache[(i, currsum)] = max(exclude, include)
        #     return cache[(i, currsum)]
        # return dfs(0, 0)
