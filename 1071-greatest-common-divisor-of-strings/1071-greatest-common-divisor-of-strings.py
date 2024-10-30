class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        n1, n2 = len(str1), len(str2)
        
        def gcd(a, b):
            if a == 0:
                return b
            return gcd(b % a, a)

        num = gcd(n1, n2)
        t = str1[:num]
        if t * (n1 // num) == str1 and t * (n2 // num) == str2:
            return t
        return ""
    