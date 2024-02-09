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
        def backtrack(i, tmp):
            if i == N:
                res.append("".join(tmp))
                return
            possibilities = mapping[digits[i]]
            for letter in possibilities:
                tmp.append(letter)
                backtrack(i + 1, tmp)
                tmp.pop()
        
        backtrack(0, [])
        if len(res) == 1 and res[0] == "":
            return ""
        return res
