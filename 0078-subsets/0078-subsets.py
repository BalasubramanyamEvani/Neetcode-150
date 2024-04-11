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
        def dfs(index, tmp):
            ret.append(tmp[:])
            for i in range(index + 1, N):
                tmp.append(nums[i])
                dfs(i, tmp)
                tmp.pop()
        dfs(-1, [])
        return ret
