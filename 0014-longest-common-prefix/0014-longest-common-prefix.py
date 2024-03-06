class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        minlen = math.inf
        mins = ""
        minsindex = -1
        for i, s in enumerate(strs):
            if len(s) < minlen:
                minlen = len(s)
                minis = s
                miniindex = i
        prefix = []
        for j, ch in enumerate(minis):
            for i in range(len(strs)):
                if strs[i][j] != minis[j]:
                    return "".join(prefix)
            prefix.append(minis[j])
        return "".join(prefix)
