class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        ptr1, ptr2 = 0, 0
        ret = []
        switch = False
        while ptr1 < len(word1) and ptr2 < len(word2):
            if not switch:
                ret.append(word1[ptr1])
                ptr1 += 1
            else:
                ret.append(word2[ptr2])
                ptr2 += 1
            switch = ~switch
        while ptr1 < len(word1):
            ret.append(word1[ptr1])
            ptr1 += 1
        while ptr2 < len(word2):
            ret.append(word2[ptr2])
            ptr2 += 1
        return "".join(ret)
