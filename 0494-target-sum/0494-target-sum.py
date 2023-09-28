class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        n = len(nums) - 1
        memo = {}
        
        def recurse(index, total):
            if index == n + 1:
                if total == target:
                    return 1
                return 0
            
            if (index, total) in memo:
                count = memo[(index, total)]
                return count
            
            memo[(index, total)] = recurse(index + 1, total + nums[index]) + recurse(index + 1, total - nums[index])
            
            return memo[(index, total)]
        
        res = recurse(0, 0)
        return res
            