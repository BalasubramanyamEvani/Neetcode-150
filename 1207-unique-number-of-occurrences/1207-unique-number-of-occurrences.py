class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        counts = Counter(arr)
        seen = set()
        for k, v in counts.items():
            if v in seen:
                return False
            seen.add(v)
        return True
