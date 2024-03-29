class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(s, e):
            while s < e:
                nums[s], nums[e] = nums[e], nums[s]
                s += 1
                e -= 1
        k = k % len(nums) 
        reverse(0, len(nums) - 1)
        reverse(0, k - 1)
        reverse(k, len(nums) - 1)
            