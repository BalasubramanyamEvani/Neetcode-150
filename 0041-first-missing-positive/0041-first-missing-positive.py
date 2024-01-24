class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        A = nums
        A = [max(num, 0) for num in A]
        for i, num in enumerate(A):
            curr = num
            # at most run 2 times - only scan [1 .. len(A) + 1]
            while curr - 1 >= 0 and curr - 1 < len(A) and A[curr - 1] != curr:
                tmp = A[curr - 1]
                A[curr - 1] = curr
                curr = tmp
        for i, num in enumerate(A):
            if i != num - 1:
                return i + 1
        return len(A) + 1
