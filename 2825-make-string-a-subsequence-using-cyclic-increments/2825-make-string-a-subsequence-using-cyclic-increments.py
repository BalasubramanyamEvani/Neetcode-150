class Solution:
    def canMakeSubsequence(self, str1: str, str2: str) -> bool:
        def cyclic_increment(ch):
            if ch == "z":
                return "a"
            ret = chr(ord(ch) + 1)
            return ret
        
        ptr1, ptr2 = 0, 0
        n1, n2 = len(str1), len(str2)
        while ptr1 < n1 and ptr2 < n2:
            if str1[ptr1] == str2[ptr2] or cyclic_increment(str1[ptr1]) == str2[ptr2]:
                ptr2 += 1
            ptr1 += 1
        return ptr2 == n2
