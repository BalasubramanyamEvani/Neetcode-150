class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        # N = len(nums)
        # M = 2**N
        # ret = []
        # for i in range(M):
        #     tmp = []
        #     for j in range(N):
        #         if (i & (1 << j)) != 0:
        #             tmp.append(nums[j])
        #     ret.append(tmp)
        # return ret
        ret = []
        N = len(nums)
        def backtrack(tmp, ind):
            ret.append(tmp[:])
            for i in range(ind, N):
                tmp.append(nums[i])
                backtrack(tmp, i + 1)
                tmp.pop()
        
        backtrack([], 0)
        return ret
