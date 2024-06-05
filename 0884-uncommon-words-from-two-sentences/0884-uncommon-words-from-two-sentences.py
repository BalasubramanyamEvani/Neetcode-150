class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        mem1 = Counter(s1.split())
        mem2 = Counter(s2.split())
        potential_words_mem1 = [key for key in mem1 if mem1[key] == 1]
        potential_words_mem2 = [key for key in mem2 if mem2[key] == 1]
        words = set([*potential_words_mem1, *potential_words_mem2])
        ret = []
        for word in words:
            f1 = word in mem1
            f2 = word in mem2
            if f1 ^ f2:
                ret.append(word)
        return ret
