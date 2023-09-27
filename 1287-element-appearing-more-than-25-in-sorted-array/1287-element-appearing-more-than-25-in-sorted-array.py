class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        thresh = 0.25 * len(arr)
        
        def bsearch(num):
            low = 0
            high = len(arr) - 1
            while low <= high:
                mid = low + (high - low) // 2
                if arr[mid] <= num:
                    low = mid + 1
                else:
                    high = mid - 1
            return low - 1
        
        for i, num in enumerate(arr):
            j = bsearch(num)
            if j - i + 1 > thresh:
                return num
        return -1
