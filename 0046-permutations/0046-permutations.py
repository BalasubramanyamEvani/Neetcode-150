class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        ret = []
        N = len(nums)
        valid = [True for _ in range(N)]
        def dfs(tmp):
            if len(tmp) == N:
                ret.append(tmp[:])
                return
            for i, num in enumerate(nums):
                if valid[i]:
                    tmp.append(num)
                    valid[i] = False
                    dfs(tmp)
                    tmp.pop()
                    valid[i] = True
        dfs([])
        return ret
