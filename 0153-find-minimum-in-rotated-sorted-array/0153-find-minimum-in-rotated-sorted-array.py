class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1
        while low <= high:
            mid = low + (high - low) // 2
            if nums[mid] <= nums[-1]:
                high = mid - 1
            else:
                low = mid + 1
        
        min1 = nums[0]
        min2 = nums[low]
        
        return min(min1, min2)
