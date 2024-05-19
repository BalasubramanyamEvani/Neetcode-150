class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        N = len(nums)
        cache = {}
        def dfs(i, currsum):
            if i == N:
                return currsum == halfSum
            if currsum == halfSum:
                return True
            if currsum > halfSum:
                return False
            if (i, currsum) in cache:
                return cache[(i, currsum)]
            exclude = dfs(i + 1, currsum)
            if exclude:
                cache[(i, currsum)] = True
                return True
            include = dfs(i + 1, currsum + nums[i])
            cache[(i, currsum)] = exclude or include
            return cache[(i, currsum)]
        
        totalSum = sum(nums)
        if totalSum % 2 != 0:
            return False
        halfSum = totalSum // 2
        return dfs(0, 0)
