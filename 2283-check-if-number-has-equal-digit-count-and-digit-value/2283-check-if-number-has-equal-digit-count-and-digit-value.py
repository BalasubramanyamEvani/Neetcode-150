class Solution:
    def digitCount(self, num: str) -> bool:
        cache = defaultdict(int)
        for ch in num:
            cache[ch] += 1
        for digit, occ in enumerate(num):
            digit = str(digit)
            occ = int(occ)
            if cache[digit] != occ:
                return False
        return True
