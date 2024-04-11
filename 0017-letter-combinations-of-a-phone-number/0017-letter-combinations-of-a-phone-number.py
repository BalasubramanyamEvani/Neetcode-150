class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        res = []
        N = len(digits)
        def dfs(i, tmp):
            if i == N:
                res.append("".join(tmp))
                return
            letters = mapping[digits[i]]
            for letter in letters:
                tmp.append(letter)
                dfs(i + 1, tmp)
                tmp.pop()
        
        dfs(0, [])
        if len(res) == 1 and res[0] == "":
            return ""
        return res
        