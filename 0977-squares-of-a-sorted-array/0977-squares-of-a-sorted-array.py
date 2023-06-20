class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        negs = []
        pos = []
        for num in nums:
            if num < 0:
                negs.append(num**2)
            else:
                pos.append(num**2)
        negs = negs[::-1]
        i = 0
        j = 0
        res = []
        while i < len(negs) and j < len(pos):
            if negs[i] < pos[j]:
                res.append(negs[i])
                i += 1
            else:
                res.append(pos[j])
                j += 1
        while i < len(negs):
            res.append(negs[i])
            i += 1
        while j < len(pos):
            res.append(pos[j])
            j += 1
        return res
        