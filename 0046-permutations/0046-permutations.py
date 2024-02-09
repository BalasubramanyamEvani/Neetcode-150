class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        valid = [True] * N
        ret = []
        def backtrack(i, tmp):
            if i == N:
                ret.append(tmp[:])
                return
            for j in range(N):
                if valid[j]:
                    tmp.append(nums[j])
                    valid[j] = False
                    backtrack(i + 1, tmp)
                    tmp.pop()
                    valid[j] = True
        backtrack(0, [])
        return ret
