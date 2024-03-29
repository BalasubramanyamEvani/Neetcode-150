class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        mem = set()
        for num in nums1:
            mem.add(num)
        ret = set()
        for num in nums2:
            if num in mem and not num in ret:
                ret.add(num)
        return list(ret)
        