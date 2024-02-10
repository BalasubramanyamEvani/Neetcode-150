class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        # Recursion - TLE
        counts = {}
        maxnum = -1
        for num in nums:
            counts[num] = counts.get(num, 0) + 1
            maxnum = max(maxnum, num)
            
        # def recursion(num, tmp):
            # if num < 1:
            #     return tmp
            # currcount = 0
            # if num in counts:
            #     currcount = counts[num]
            # curr = currcount * num
            # l = recursion(num - 1, tmp)
        #     r = recursion(num - 2, tmp + curr)
        #     return max(l, r)
        # return recursion(maxnum, 0)
        
        # Top Down - Memoization
        # memo = {}
        # def recursion(num, tmp):
        #     if num < 1:
        #         return tmp
        #     if num in memo:
        #         return tmp + memo[num]
        #     currcount = 0
        #     if num in counts:
        #         currcount = counts[num]
        #     curr = currcount * num
        #     l = recursion(num - 1, tmp)
        #     r = recursion(num - 2, tmp + curr)
        #     memo[num] = max(l, r)
        #     return memo[num]
        # return recursion(maxnum, 0)
        
        #Bottom Up - Tabular
        dp = [0 for _ in range(maxnum + 1)]
        dp[1] = counts.get(1, 0)
        for i in range(2, maxnum + 1):
            dp[i] = max(dp[i - 1], dp[i - 2] + i * counts.get(i, 0))
        return dp[-1]
