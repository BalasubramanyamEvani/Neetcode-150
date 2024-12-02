class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        seen = Counter(arr)
        for num in seen:
            if 2 * num in seen:
                if num != 2 * num:
                    return True
                if seen[num] > 1:
                    return True
        return False
