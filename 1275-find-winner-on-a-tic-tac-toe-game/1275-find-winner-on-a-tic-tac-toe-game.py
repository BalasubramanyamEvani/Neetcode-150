class Solution:
    def tictactoe(self, moves: List[List[int]]) -> str:
        num_moves = len(moves)
        grid = [[""] * 3 for _ in range(3)]
        state = True
        for move in moves:
            r, c = move
            grid[r][c] = "x" if state else "o"
            state = not state
            
        awins = "xxx"
        bwins = "ooo"
        winspace = ["".join(row) for row in grid] + ["".join([grid[i][i] for i in range(3)])] + ["".join([grid[2 - i][i] for i in range(2, -1, -1)])]
        for i in range(3):
            tmp = []
            for j in range(3):
                tmp.append(grid[j][i])
            winspace.append("".join(tmp))
        
        if awins in winspace:
            return "A"
        if bwins in winspace:
            return "B"
        if num_moves == 9:
            return "Draw"
        return "Pending"
        