class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        nr = len(words)
        nc = max([len(word) for word in words])

        for i in range(nc):
            tmp = []
            for j in range(nr):
                if i >= len(words[j]):
                    break
                tmp.append(words[j][i])
            colword = "".join(tmp)
            if colword != words[i]:
                return False
        return True
