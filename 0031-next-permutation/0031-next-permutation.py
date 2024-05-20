class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        N = len(nums)
        pivot = None
        for i in range(N - 1, 0, -1):
            if nums[i] > nums[i - 1]:
                pivot = i - 1
                break
        if pivot is None:
            return nums.reverse()
        swap = N - 1
        while nums[swap] <= nums[pivot]:
            swap -= 1
        nums[swap], nums[pivot] = nums[pivot], nums[swap]
        nums[pivot + 1:] = nums[pivot + 1:][::-1]
        return nums
