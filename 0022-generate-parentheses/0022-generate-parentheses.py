class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        res = []
        
        def backtrack(curr, opench, closech):
            if len(curr) == 2 * n:
                res.append("".join(curr))
                return
            
            if closech < n and closech < opench:
                curr.append(")")
                backtrack(curr, opench, closech + 1)
                curr.pop()
            
            if opench < n:
                curr.append("(")
                backtrack(curr, opench + 1, closech)
                curr.pop()

            return
        
        backtrack([], 0, 0)
        return res
