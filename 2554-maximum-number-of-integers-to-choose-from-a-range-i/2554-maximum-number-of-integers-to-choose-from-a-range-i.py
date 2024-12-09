class Solution:
    def maxCount(self, banned: List[int], n: int, maxSum: int) -> int:
        numbers = []
        banned = set(banned)
        num_sum = 0
        for i in range(1, n + 1):
            if i in banned:
                continue
            if num_sum + i > maxSum:
                break
            numbers.append(i)
            num_sum += i
        return len(numbers)
