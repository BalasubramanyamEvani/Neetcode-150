class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        n = len(nums)
        dp = [0] * n
        
        for i in range(n):
            curr_max = dp[i]
            for j in range(i):
                if nums[j] < nums[i]:
                    curr_max = max(dp[j], curr_max)
            
            dp[i] = 1 + curr_max
        
        return max(dp)
