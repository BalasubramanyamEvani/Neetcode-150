class Solution:
    def rob(self, nums: List[int]) -> int:
        tot_houses = len(nums)
        dp = [0] * tot_houses
        dp[0] = nums[0]
        for i in range(1, len(nums)):
            dp[i] = max(dp[i - 1], nums[i] + (dp[i - 2] if i - 2 >= 0 else 0))
        return dp[-1]
