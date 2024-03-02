class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        ones = 0
        N = len(s)
        for ch in s:
            if ch == "1":
                ones += 1
        lsb = 1 if ones >= 1 else 0
        zeros = N - ones
        ones = ones - lsb
        return "1" * ones + "0" * zeros + "1" * lsb
