class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * 366
        lastday = days[-1]
        firstday = days[0]
        i = 0
        for day in range(firstday, lastday + 1):
            if day == days[i]: 
                dp[day] = min(
                    dp[day - 1] + costs[0],
                    dp[max(0, day - 7)] + costs[1],
                    dp[max(0, day - 30)] + costs[2],
                )
                i += 1
            else:
                dp[day] = dp[day - 1]
        return dp[lastday]
