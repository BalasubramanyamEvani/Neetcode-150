class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        nums1idx = {}
        for i, num in enumerate(nums1):
            nums1idx[num] = i
        
        res = [-1] * len(nums1)
        
        stack = deque()
        for i, num in enumerate(nums2):
            curr = num
            while stack and curr > stack[-1]:
                val = stack.pop()
                idx = nums1idx[val]
                res[idx] = curr
            
            if curr in nums1idx:
                stack.append(curr)
        
        return res
