class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        N = len(nums)
        ret = [0 for _ in range(N)]
        pos = 0
        neg = 1
        for num in nums:
            if num > 0:
                ret[pos] = num
                pos += 2
            else:
                ret[neg] = num
                neg += 2
        return ret
