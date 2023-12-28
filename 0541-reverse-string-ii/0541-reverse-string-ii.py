class Solution:
    def reverseStr(self, s: str, k: int) -> str: 
        sret = list(s)
        slen = len(sret)
        for i in range(0, slen, 2*k):
            sret[i:i+k] = reversed(sret[i:i+k])
        return "".join(sret)
