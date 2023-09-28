class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def bsearch(l, h):
            while l <= h:
                m = l + (h - l) // 2
                if nums[m] == target:
                    return m
                if nums[m] < target:
                    l = m + 1
                else:
                    h = m - 1
            return -1
        
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] <= nums[-1]:
                high = mid - 1
            else:
                low = mid + 1
        
        bp = low
        ret = bsearch(0, low - 1)
        if ret != -1:
            return ret

        return bsearch(low, len(nums) - 1)
        