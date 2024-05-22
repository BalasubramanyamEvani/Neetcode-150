class Solution:
    def rob(self, nums: List[int]) -> int:
        def robIt(houses):
            N = len(houses)
            dp = [0] * N
            dp[0] = houses[0]
            for i in range(1, N):
                rob = houses[i]
                if i - 2 >= 0:
                    rob += dp[i - 2]
                notrob = dp[i - 1]
                dp[i] = max(rob, notrob)
            return dp[-1]
        M = len(nums)
        if M == 1:
            return nums[0]
        return max(robIt(nums[1:]), robIt(nums[:M-1]))
