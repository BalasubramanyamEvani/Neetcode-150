class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        N1, N2 = len(str1), len(str2)
        mins = str1
        if N2 < N1:
            mins = str2
        start = min(N1, N2)
        def isDivisor(num):
            if N1 % num != 0 or N2 % num != 0:
                return False
            f1, f2 = N1 // num, N2 // num
            return mins[:num] * f1 == str1 and mins[:num] * f2 == str2
        
        for i in range(start, 0, -1):
            if isDivisor(i):
                return mins[:i]
        return ""
