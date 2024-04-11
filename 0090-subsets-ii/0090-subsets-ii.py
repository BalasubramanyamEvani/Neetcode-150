class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ret = []
        # sort in increasing order
        # to make sure we don't visit
        # numbers already visited after
        # certain index
        nums.sort()
        N = len(nums)
        def dfs(index, tmp):
            ret.append(tmp[:])
            for i in range(index + 1, N):
                # this is where the check happens
                if nums[i] == nums[i - 1] and i - 1 != index:
                    continue
                tmp.append(nums[i])
                dfs(i, tmp)
                tmp.pop()
        dfs(-1, [])
        return ret
