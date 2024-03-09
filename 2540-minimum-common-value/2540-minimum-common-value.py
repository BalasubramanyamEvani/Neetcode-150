class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        ptr1 = 0
        ptr2 = 0
        N1, N2 = len(nums1), len(nums2)
        while ptr1 < N1 and ptr2 < N2:
            if nums1[ptr1] < nums2[ptr2]:
                ptr1 += 1
            elif nums2[ptr2] < nums1[ptr1]:
                ptr2 += 1
            else:
                return nums1[ptr1]
        return -1
