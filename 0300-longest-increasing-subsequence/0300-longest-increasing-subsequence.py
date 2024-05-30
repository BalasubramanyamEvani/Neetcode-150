class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # N = len(nums)
        # LIS = [1] * N
        # for i in range(N - 1, -1, -1):
        #     for j in range(i + 1, N):
        #         if nums[i] < nums[j]:
        #             LIS[i] = max(LIS[i], 1 + LIS[j])
        # return max(LIS)
        N = len(nums)
        dp = [1] * N
        for i in range(1, N):
            for j in range(i):
                if nums[j] < nums[i]:
                    dp[i] = max(dp[i], 1 + dp[j])
        return max(dp)
        
#         N = len(nums)
#         @cache
#         def dfs(i, prevIndex):
#             if i == N:
#                 return 0
#             ret = -math.inf
#             # dont take
#             ret = max(ret, 0 + dfs(i + 1, prevIndex))
#             # take
#             if prevIndex == -1 or nums[prevIndex] < nums[i]:
#                 ret = max(ret, 1 + dfs(i + 1, i))
#             return ret
        
#         return dfs(0, -1)

