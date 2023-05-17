class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        forward_prod = [0] * n
        backward_prod = [0] * n
        prod = 1
        for i in range(n):
            forward_prod[i] = prod * (nums[i - 1] if i - 1 >= 0 else 1)
            prod = forward_prod[i]
        prod = 1
        for i in range(n - 1, -1, -1):
            backward_prod[i] = prod * (nums[i + 1] if i + 1 <= n - 1 else 1)
            prod = backward_prod[i]
        res = [0] * n
        for i in range(n):
            res[i] = forward_prod[i] * backward_prod[i]
        return res
