class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        nr, nc = len(board), len(board[0])
        
        def dfs(res, r, c, index):
            if len(res) == len(word):
                return "".join(res) == word
            
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return False
            
            if word[index] != board[r][c]:
                return False
            
            dr = [-1, 1, 0, 0]
            dc = [0 ,0, -1, 1]
            
            res.append(board[r][c])
            board[r][c] = "#"
            
            for i in range(4):
                if dfs(res, r + dr[i], c + dc[i], index + 1):
                    return True
            
            board[r][c] = res.pop(-1)
            
            return False
        
        for i in range(nr):
            for j in range(nc):
                if dfs([], i, j, 0):
                    return True
        
        return False
