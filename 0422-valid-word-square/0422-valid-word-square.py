class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        col_words = []
        nr = len(words)
        nc = max([len(word) for word in words])

        for i in range(nc):
            tmp = []
            for j in range(nr):
                if i >= len(words[j]):
                    break
                tmp.append(words[j][i])
            col_words.append("".join(tmp))
        
        for i in range(nr):
            if words[i] != col_words[i]:
                return False
        return True
