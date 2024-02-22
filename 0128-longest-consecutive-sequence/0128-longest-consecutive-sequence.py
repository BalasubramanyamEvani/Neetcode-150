class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        nums = set(nums)
        lcs = -math.inf
        for num in nums:
            if num - 1 not in nums:
                maxlen = 1
                currnum = num
                while currnum + 1 in nums:
                    maxlen += 1
                    currnum = currnum + 1
                lcs = max(lcs, maxlen)
        return lcs
