class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nr, nc = len(board), len(board[0])
        visited = set()
        def dfs(r, c):
            if r < 0 or r >= nr or c < 0 or c >= nc:
                return
            if board[r][c] == "O" and (r, c) not in visited:
                visited.add((r, c))
                dfs(r + 1, c)
                dfs(r - 1, c)
                dfs(r, c + 1)
                dfs(r, c - 1)
        
        # similar to pacific atlantic
        # only those which have "O" connected till
        # the boundary will not be surrounded by "X"
        # from 4 sides
        for i in range(nr):
            if board[i][0] == "O" and (i, 0) not in visited: 
                dfs(i, 0)
            if board[i][nc - 1] == "O" and (i, nc - 1) not in visited:
                dfs(i, nc - 1)
        
        for i in range(nc):
            if board[0][i] == "O" and (0, i) not in visited: 
                dfs(0, i)
            if board[nr - 1][i] == "O" and (nr - 1, i) not in visited:
                dfs(nr - 1, i)
        
        for i in range(nr):
            for j in range(nc):
                if (i, j) not in visited:
                    board[i][j] = "X"
