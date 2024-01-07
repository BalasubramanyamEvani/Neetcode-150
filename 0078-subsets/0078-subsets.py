class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        N = len(nums)
        M = 2**N
        ret = []
        for i in range(M):
            tmp = []
            for j in range(N):
                if (i & (1 << j)) != 0:
                    tmp.append(nums[j])
            ret.append(tmp)
        return ret
