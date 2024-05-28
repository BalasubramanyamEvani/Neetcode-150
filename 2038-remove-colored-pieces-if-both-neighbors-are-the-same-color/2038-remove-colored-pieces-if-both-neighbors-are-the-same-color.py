class Solution:
    def winnerOfGame(self, colors: str) -> bool:
        N = len(colors)
        A, B = 0, 0
        for i in range(1, N - 1):
            if colors[i] == colors[i - 1] == colors[i + 1]:
                if colors[i] == "A":
                    A += 1
                else:
                    B += 1
        return A > B
