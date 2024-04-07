class Solution:
    def checkValidString(self, s: str) -> bool:
        N = len(s)
        
        @cache
        def dfs(index, opened):
            if index == N:
                return opened == 0
            ch = s[index]
            if ch == ")" and opened <= 0:
                return False
            if ch == "(":
                return dfs(index + 1, opened + 1) 
            
            if ch == ")":
                return dfs(index + 1, opened - 1) 
            
            f1 = dfs(index + 1, opened + 1)
            f2 = False
            if opened > 0:
                f2 = dfs(index + 1, opened - 1)
            f3 = dfs(index + 1, opened)
            return f1 or f2 or f3
        
        return dfs(0, 0)
