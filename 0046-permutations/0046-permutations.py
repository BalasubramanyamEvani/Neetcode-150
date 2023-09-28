class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        n = len(nums)
        ret = []
        valid = [True] * n
        
        def backtrack(res):
            if len(res) == n:
                ret.append(res[:])
                return
            for i in range(n):
                if valid[i]:
                    res.append(nums[i])
                    valid[i] = False
                    backtrack(res)
                    valid[i] = True
                    res.pop(-1)
        
        backtrack([])
        return ret