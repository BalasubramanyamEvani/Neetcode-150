class Solution:
    def reverseWords(self, s: str) -> str:
        res = []
        def reverse(st):
            p = []
            j = len(st) - 1
            while j >= 0:
                p.append(st[j])
                j -= 1
            return "".join(p)
        i = 0
        while i < len(s):
            flag = False
            j = i + 1
            while j < len(s):
                if s[j] == " ":
                    res.append(reverse(s[i: j]))
                    flag = True
                    break
                j += 1
                
            if not flag:
                res.append(reverse(s[i:]))
            else:
                j += 1
            i = j
        return " ".join(res)
                    