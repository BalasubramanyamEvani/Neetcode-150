class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        set1 = set(nums1)
        set2 = set(nums2)
        ret2 = []
        for num in set2:
            if num not in set1:
                ret2.append(num)
        ret1 = []
        for num in set1:
            if num not in set2:
                ret1.append(num)
        return [ret1, ret2]
