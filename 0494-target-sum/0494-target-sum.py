class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        N = len(nums)
        cache = {}
        def dfs(i, currsum):
            if i == N:
                return 1 if currsum == target else 0
            if (i, currsum) in cache:
                return cache[(i, currsum)]
            left = dfs(i + 1, currsum + nums[i])
            right = dfs(i + 1, currsum - nums[i])
            cache[(i, currsum)] = left + right
            return left + right
        return dfs(0, 0)
