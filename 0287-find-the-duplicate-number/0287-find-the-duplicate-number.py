class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
#         def count_nums_less_than_equal(n):
#             res = 0
#             for num in nums:
#                 if num <= n:
#                     res += 1
#             return res
        
#         N = len(nums) - 1
#         low = 1
#         high = N
#         while low <= high:
#             mid = low + (high - low) // 2
#             if count_nums_less_than_equal(mid) > mid:
#                 high = mid - 1
#             else:
#                 low = mid + 1
#         return high + 1
        slow = nums[0]
        fast = nums[0]
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        ptr1 = nums[0]
        ptr2 = slow
        while ptr1 != ptr2:
            ptr1 = nums[ptr1]
            ptr2 = nums[ptr2]
        return ptr1
