class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # [10, 2, 10] [16, 5, 16]
        # dp[0] = 2, selected = 1
        # dp[1] = min(dp[0] + min(arr[1][0], arr[1][2])
        #           if arr[1] < arr[0] and arr[1] < arr[2]
        #       = arr[1] + min(arr[0][0], arr[0][1]))
        # dp[i] = min(dp[i - 1] + min(arr[i][~prev]), arr[prev] + min(arr[i - 1][~prev]))
        N = len(costs)
        cache = {}
        def dfs(i, prev_color):
            if i == N:
                return 0
            if (i, prev_color) in cache:
                return cache[(i, prev_color)]
            cost = costs[i][prev_color]
            if prev_color == 0:
                cost += min(dfs(i + 1, 1), dfs(i + 1, 2))
            if prev_color == 1:
                cost += min(dfs(i + 1, 0), dfs(i + 1, 2))
            if prev_color == 2:
                cost += min(dfs(i + 1, 0), dfs(i + 1, 1))
            cache[(i, prev_color)] = cost
            return cost

        return min(min(dfs(0, 0), dfs(0, 1)), dfs(0, 2))
