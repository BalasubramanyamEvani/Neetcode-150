class Solution:
    def canJump(self, nums: List[int]) -> bool:
        N = len(nums)
        # @cache
        # def dfs(i):
        #     if i == N - 1:
        #         return True
        #     jumps = min(N - 1, i + nums[i])
        #     for j in range(i + 1, jumps + 1):
        #         if dfs(j):
        #             return True
        #     return False
        # return dfs(0)
        
        # greedy
        currmax = 0
        for i, num in enumerate(nums):
            if i > currmax:
                return False
            currmax = max(currmax, i + nums[i])
        return currmax >= N - 1
