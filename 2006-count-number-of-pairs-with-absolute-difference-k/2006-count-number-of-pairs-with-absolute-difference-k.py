class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        mem = {}
        count = 0
        for num in nums:
            n1, n2 = num + k, num - k
            count += mem.get(n1, 0)
            count += mem.get(n2, 0)
            mem[num] = mem.get(num, 0) + 1
        return count
