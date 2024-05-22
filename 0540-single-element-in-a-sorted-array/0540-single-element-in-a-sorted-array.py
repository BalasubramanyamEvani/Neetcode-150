class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        def dfs(l, r):
            if r - l + 1 == 1:
                return nums[l]
            mid = l + (r - l) // 2
            left = dfs(l, mid)
            right = dfs(mid + 1, r)
            return left ^ right
        
        N = len(nums)
        return dfs(0, N - 1)
